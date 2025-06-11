import rumps
import pyperclip
import subprocess

PROMPT_FILE = "prompts.txt"
print("Starting PromptTool...")

class PromptTool(rumps.App):
    def __init__(self):
        super().__init__("PromptTool", icon="MyIcon.icns")
        self.categorized_prompts = self.load_prompts()
        self.menu.clear()

        for category, prompts in self.categorized_prompts.items():
            if category: # If it's a category, add it as a submenu
                self.menu.add(rumps.MenuItem(category))
                for summary, prompt_text in prompts:
                    self.menu.add(rumps.MenuItem(summary, callback=self.copy_prompt))
            else: # For prompts without a category (if you choose to support them)
                for summary, prompt_text in prompts:
                    self.menu.add(rumps.MenuItem(summary, callback=self.copy_prompt))
            self.menu.add(rumps.separator) # Add a separator after each category

    def load_prompts(self):
        categorized_prompts = {}
        current_category = "" # Initialize with an empty string for uncategorized prompts
        try:
            with open(PROMPT_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith("###"):
                        current_category = line[3:].strip()
                        categorized_prompts[current_category] = []
                    elif ':::' in line:
                        if not current_category: # Handle prompts before any category is defined
                            if "Uncategorized" not in categorized_prompts:
                                categorized_prompts["Uncategorized"] = []
                            summary, prompt = line.split(":::", 1)
                            categorized_prompts["Uncategorized"].append((summary.strip(), prompt.strip()))
                        else:
                            summary, prompt = line.split(":::", 1)
                            categorized_prompts[current_category].append((summary.strip(), prompt.strip()))
                    else:
                        print(f"Skipping malformed line: {line.strip()}")

            if not categorized_prompts:
                rumps.alert("No valid prompts or categories found in the file.")
        except FileNotFoundError:
            rumps.alert("Prompt file not found.")
        return categorized_prompts

    def show_notification(self, title, message):
        safe_title = title.replace('"', '\\"')
        safe_message = message.replace('"', '\\"')
        subprocess.run([
            "osascript", "-e",
            f'display notification "{safe_message}" with title "{safe_title}"'
        ])

    def copy_prompt(self, sender):
        # To get the prompt text, we now need to iterate through categories
        prompt_text = None
        for category, prompts in self.categorized_prompts.items():
            for summary, text in prompts:
                if summary == sender.title:
                    prompt_text = text
                    break
            if prompt_text:
                break

        if prompt_text:
            pyperclip.copy(prompt_text)
            self.show_notification("Copied!", sender.title)


if __name__ == "__main__":
    print("Running app...")
    PromptTool().run()
