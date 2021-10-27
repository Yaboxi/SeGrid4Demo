from selenium import webdriver


class TestGrid:
    def choose_driver(self, browser: str) -> webdriver:
        command_executor = "http://localhost:4444"

        if browser == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser == "edge":
            options = webdriver.edge.options.Options()
        else: # chrome
            options = webdriver.ChromeOptions()

        options.set_capability("se:recordVideo", "true")
        options.set_capability("se:timeZone", "JST")

        driver = webdriver.Remote(
            command_executor=command_executor,
            options=options,
        )

        driver.set_window_size(1024, 768)

        return driver

    def test_chrome(self):
        driver = self.choose_driver("chrome")

        driver.get('http://whatsmyuseragent.org/')
        driver.save_screenshot("./results/google.png")

        driver.quit()

        assert True

    def test_firefox(self):
        driver = self.choose_driver("firefox")

        driver.get('http://whatsmyuseragent.org/')
        driver.save_screenshot("./results/firefox.png")

        driver.quit()

        assert True

    def test_edge(self):
        driver = self.choose_driver("edge")

        driver.get('http://whatsmyuseragent.org/')
        driver.save_screenshot("./results/edge.png")

        driver.quit()

        assert True
