# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest
import time


class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "r")))
            body = self.driver.page_source
            return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        except Exception as e:
            # Timeout on WebDriverWait
            raise IgnoreRequest
