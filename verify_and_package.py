"""Validate an Academic Research skill folder and build its import ZIP."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import yaml


SKILL_NAME = "academic-research-chatgpt"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(skill):
    source = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.fullmatch(r"---\n(.*?)\n---\n(.+)", source, re.DOTALL)
    require(match is not None, "SKILL.md must have YAML frontmatter and a body")
    frontmatter = yaml.safe_load(match[1])
    require(set(frontmatter) == {"name", "description"}, "Unexpected frontmatter fields")
    require(
        frontmatter["name"] == SKILL_NAME == skill.name
        and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name)
        and len(skill.name) <= 64,
        "Skill name and directory must match the Agent Skills naming rules",
    )
    description = frontmatter["description"]
    require(isinstance(description, str) and 0 < len(description.strip()) <= 1024,
            "Invalid skill description")
    require(len(source.splitlines()) <= 500, "Keep the entry point under 500 lines")

    manifest = json.loads((skill / "manifest.json").read_text(encoding="utf-8"))
    references = {file.name for file in (skill / "references").glob("*.md")}
    require(set(manifest["references"]) == references, "Manifest reference list differs from disk")
    entry_links = set(re.findall(r"\]\(references/([^\s)]+)\)", match[2]))
    require(entry_links == references, "The main entry must link to every reference")
    require("writing.md" in references, "Missing the writing reference")

    for document in sorted(skill.rglob("*.md")):
        body = document.read_text(encoding="utf-8")
        require(body.strip(), f"Empty Markdown file: {document}")
        for raw_target in re.findall(r"\]\(([^\s)]+)\)", body):
            target = urlsplit(raw_target)
            if not target.scheme and not target.netloc and target.path:
                destination = (document.parent / target.path).resolve()
                require(destination.is_relative_to(skill) and destination.is_file(),
                        f"Invalid relative link in {document}: {raw_target}")

    agent = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    require(agent["policy"]["allow_implicit_invocation"] is True, "Implicit invocation disabled")
    for icon in ("icon_small", "icon_large"):
        require((skill / agent["interface"][icon]).is_file(), f"Missing {icon}")
    require((skill / "LICENSE").read_text(encoding="utf-8").startswith(
        "Copyright (c) 2026 Cheng-I Wu\n"), "Missing upstream license and attribution")
    return manifest["adapter_version"], len(references)


def package(skill, output):
    files = sorted(path for path in skill.rglob("*") if path.is_file())
    names = [path.relative_to(skill.parent).as_posix() for path in files]
    with ZipFile(output, "w") as archive:
        for path, name in zip(files, names, strict=True):
            require(not path.is_symlink(), f"Cannot package symlink: {path}")
            member = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            member.external_attr = 0o100644 << 16
            archive.writestr(member, path.read_bytes(), compress_type=ZIP_DEFLATED)
    with ZipFile(output) as archive:
        require(archive.testzip() is None, "ZIP CRC verification failed")
        require(archive.namelist() == names, "Unexpected ZIP members")
        for path, name in zip(files, names, strict=True):
            require(archive.read(name) == path.read_bytes(), f"Archive content mismatch: {name}")
    return len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    skill = args.skill.resolve()
    version, references = validate(skill)
    members = package(skill, args.output)
    print(f"Validated {SKILL_NAME} {version}: {references} references, {members} ZIP files")


if __name__ == "__main__":
    main()
