package com.Selenium;

import org.openqa.selenium.chrome.ChromeDriver;

public class Main
{

    public static void main(String[] args) throws InterruptedException {
        String login = "Maniek13MT";
        String haslo = "Test123456";

        //Użycie pliku chromedriver.exe
        String chromedriverPath = "C:\\Users\\kursant\\Desktop\\auto\\chromedriver\\chromedriver.exe";
        System.setProperty("webdriver.chrome.driver", chromedriverPath);

        //Definicja sterownika do Chrome
        ChromeDriver driver = new ChromeDriver();
	// Definicja obiektu
        Console console = new Console();
        //console.MethodIf();
        //console.MethodFor();

     //   Bing bing = new Bing();
    //    bing.BingMethod();

        Roundcube roundcube = new Roundcube();
        //roundcube.CreateNewUser(driver);
        roundcube.LoginUser(driver,login,haslo);
        roundcube.SendMail(driver,login);
    }
}
