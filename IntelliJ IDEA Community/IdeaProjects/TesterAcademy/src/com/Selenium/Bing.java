package com.Selenium;
import org.openqa.selenium.Keys;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.support.ui.*;
import org.openqa.selenium.chrome.ChromeDriver;


public class Bing
{
    public void BingMethod()
    {
        //Użycie pliku chromedriver.exe
        String chromedriverPath = "C:\\Users\\kursant\\Desktop\\auto\\chromedriver\\chromedriver.exe";
        System.setProperty("webdriver.chrome.driver", chromedriverPath);

        //Definicja sterownika do Chrome
        ChromeDriver driver = new ChromeDriver();
        //Komunikat
        System.out.println("Start Bing Method");
        //Otworzenie danej strony WWW
        driver.get("https://www.bing.com/");
        //Powiększenie okna przeglądarki
        driver.manage().window().maximize();

        //driver.findElementByClassName("sb_form_q").sendKeys("Sii Polska");
        //driver.findElementById("sb_form_q").sendKeys(Keys.ENTER);

        //driver.findElementByClassName("sb_form_q").sendKeys("Sii Polska");
        //driver.findElementById("sb_form_q").sendKeys(Keys.ENTER);

        //driver.findElementByName("q").sendKeys("Sii Polska");
        //driver.findElementById("sb_form_q").sendKeys(Keys.ENTER);

        driver.findElementByName("q").sendKeys("Sii Polska");
        driver.findElementByXPath("//*[@id=\"search_icon\"]").click();

    }


}
