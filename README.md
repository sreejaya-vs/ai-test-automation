# 🚀 AI-Powered Test Automation Generator

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Appium](https://img.shields.io/badge/Appium-2.0%2B-green)](https://appium.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-purple)](https://openai.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/sreejaya-vs/ai-test-automation.git/pulls)

**Transform User Stories & Figma Designs → Automated Test Scripts with AI**

## 🌟 Key Features
| Feature | Description |
|---------|-------------|
| 🤖 AI Test Generation | Convert user stories to executable test cases |
| 🎨 Figma Integration | Auto-generate locators from design files |
| 🔄 Self-Healing Tests | Automatic locator recovery |
| 📱 Cross-Platform | Android & iOS support |
| 👁️ Visual Testing | Figma vs implementation comparison |
| 📝 BDD Support | Gherkin feature files |
| ⚙️ CI/CD Ready | GitHub Actions & Allure Reports |

## 🛠️ Installation
### Prerequisites
- Python 3.9+
- Appium Server 2.0+
- Node.js
- OpenAI API key
- Figma access token

```bash
# Clone repository
https://github.com/sreejaya-vs/ai-test-automation.git
cd ai-test-automation

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp
```

## Edit .env with your API keys:
```
env
OPENAI_API_KEY=your_key_here
FIGMA_TOKEN=your_token_here
```

## 🚦 Quick Start
 Add your input files:
   1. Place user stories in input/user_stories/
   2. Add APK/IPA files to apk_ipa_files/

## Run the generator:
```
bash
python main.py
```

## Follow prompts to input:

1. User story path
2. Figma file URL
3. App binary path

## Execute generated tests:
```
bash
pytest output/appium_scripts/ --alluredir=reports
```

## 📂 Project Structure
text
ai-test-automation/
├── config/               # Configuration files
├── input/                # User stories and Figma links
├── output/               # Generated test cases and scripts
├── apk_ipa_files/        # Mobile application binaries
├── tests/                # Unit and integration tests
├── .github/workflows/    # CI/CD pipelines
├── main.py               # Main entry point
└── README.md


## 🔧 Advanced Configuration

Customize config/config.yaml for:
   1. Different LLM models (GPT-4, Gemini, etc.)
   2. Appium capabilities
   3. Self-healing strategies
   4. Locator priority

Example:
```
yaml
llm_model: "gpt-4"
appium:
  platformName: "iOS"
  deviceName: "iPhone 15"
self_healing: True
```

## 🤝 Contributing

I welcome contributions! Please follow these steps:

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See LICENSE for more information.

## 📞 Contact
Project Maintainer - Sreejaya V S

Project Link: (https://github.com/sreejaya-vs/ai-test-automation.git)

## 🙏 Acknowledgments
1. OpenAI for their amazing language models
2. Appium community for mobile test automation
3. Figma for design collaboration tools
