# Academic Research for ChatGPT

Independent ChatGPT adaptation of Cheng-I Wu's [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills), distributed under [CC BY-NC 4.0](academic-research-chatgpt/LICENSE). See the [provenance record](academic-research-chatgpt/references/provenance.md) for source revisions and adaptation details.

## 安装与更新

- 已有同名技能时，先打开 ChatGPT 的 **Plugins → Skills → Created by me**，检查原条目能否打开。需要更新时，优先在原条目使用该账号提供的编辑方式，避免出现两个同名技能。
- 如果需要新安装，在支持上传的账号和工作区打开 **Plugins → Skills → Create → Upload from your computer**，上传 [academic-research-chatgpt-1.1.0.zip](academic-research-chatgpt-1.1.0.zip)。直接选 ZIP。等待扫描，按页面提示处理，并在 **Installed** 中检查该技能。
- [OpenAI 的 ChatGPT Skills 帮助](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)列出了创建、安装、编辑器及上传入口。使用本地 Codex 技能目录仅配置 Codex 的本地发现。不同产品和界面的可用性、安装和同步取决于账号与工作区。

## 验证

在同一工作区新开普通 ChatGPT 对话，不点名技能，发送“请审阅下面的论文摘要，给出总体评价、具体问题和修改方向”，并附摘要。只有界面显示可核对的技能调用记录时，才能确认自动触发。用熟悉的写作风格作答只能作为行为观察。对旧会话，可要求读取技能主说明和 `references/writing.md`，并核对实际读取记录。

本地可用 Python 3.10+ 和 PyYAML 重建 ZIP，并校验清单、相对路径和归档内容。

```bash
python verify_and_package.py academic-research-chatgpt academic-research-chatgpt-1.1.0.zip
unzip -t academic-research-chatgpt-1.1.0.zip
sha256sum academic-research-chatgpt-1.1.0.zip
```
