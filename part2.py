class BrowserHistoryStack:
    def __init__ (self):
        self.pages = []

    def open_page(self, page):
        self.pages.append(page)

    
    def delete_page(self):
        if not self.is_empty():
            self.pages.pop()
            print("\nMost recent page removed from history.\n")

    def is_empty(self):
        return len(self.pages) == 0
    
    def size(self):
        length = len(self.pages)
        return print(f"You currently have {length} pages in your history.")
    
    def show_history(self):
        if self.is_empty():
            print("There are no pages in your history.")

        else:
            for page in self.pages:
                print(f"Page: '{page}'")


browser_history = BrowserHistoryStack()

browser_history.open_page("Google")
browser_history.open_page("Facebook")
browser_history.open_page("IMDB")
browser_history.open_page("Coding Temple")

browser_history.show_history()

browser_history.delete_page()

browser_history.size()

if browser_history.is_empty():
    print("You do not have any history to display.")
else:
    browser_history.show_history()