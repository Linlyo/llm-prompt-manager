# 2506-llm-prompt-template-manager
This is a simple Mac desktop menu bar app that helps you organize the prompts that you need to use regularly.

There could be prompts that you repeated need to use when interacting with LLMs. And they may serve different purposes. 

Here's a starting point for your mind map when working with LLMs every day. This is how you'd keep your tasks organized in the `prompts.txt`.

Example:
```
### Coding
LC review:::Please assess my code for a Leetcode question from the perspective of an interview, and provide feedback.

Compare:::Compare these two versions of code. Explain the differences to me. Use examples when necessary and let me know which would be better for a tech interview.

### Writing
Edit:::Please edit this text. Do not change any content details, but only focus on the language itself. Smooth out any expression that may read awkward or unnatural, and fix any grammar issues. This will help me as a non-native speaker.

### Others
Tell Joke::: Hey, can you tell me a joke to lighten up my mood? It's been such a stressful day and I'm tried. In your joke, make sure to include a number that's the date of this month. Be creative.
```
After `###` is your category name. The label shown in the dropdown menu proceeds the actual template, separated by `:::`.

The app can be launched as a standalone app on iOS if you use the `setup.py` for the creation. After running the process, the final product will be in the folder `dist`.

Let me know if you have any suggestions.

Here's the design of the app's icon after my chill collaboration with Gemini. It looks good on the top right side of your Mac's tool bar.

![PromptTool](images/icon.png)



---
Requires Python version 3.9 or later.