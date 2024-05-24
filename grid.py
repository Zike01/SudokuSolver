from bs4 import BeautifulSoup
import requests

class Grid:
    def __init__(self):
        URL = input("Link to puzzle: ").replace("www", "west")
        html_data = requests.get(URL).text
        self.soup = BeautifulSoup(html_data, "html.parser")

    def create(self):
        grid = [[0] * 9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                try:
                    td = self.soup.find("input", id=f"f{col}{row}")["value"]
                    grid[row][col] = int(td)
                except KeyError:
                    pass
        return grid
