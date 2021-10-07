package com.Selenium;
import org.openqa.selenium.Keys;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.support.ui.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class Roundcube {

    String dd = "12";
    int mm = 2;
    String yy = "1995";
    String telephone = "060317090814";

    public void CreateNewUser(ChromeDriver driver, String login,String haslo)
    {
        //Komunikat
        System.out.println("Metoda Roundcube");
        //Otworzenie danej strony WWW
        driver.get("https://selenium.waw.pl");
        //Powiększenie okna przeglądarki
        driver.manage().window().maximize();

        driver.findElementById("rcmloginuser").sendKeys(login);
        driver.findElementById("password").sendKeys(haslo);
        driver.findElementById("confirm_password").sendKeys(haslo);

        Select day = new Select(driver.findElementByName("birthday-day"));
        day.selectByVisibleText(dd);

        Select mounth = new Select(driver.findElementByName("birthday-month"));
        mounth.selectByIndex(mm);

        Select year = new Select(driver.findElementByName("birthday-year"));
        year.selectByVisibleText(yy);

        driver.findElementByXPath("//input[@value='M']").click();
        driver.findElementByName("phone").sendKeys(telephone);
        driver.findElementById("rcmloginsubmit").click();

        }

    public void LoginUser(ChromeDriver driver, String login,String haslo) throws InterruptedException {
        driver.get("https://selenium.waw.pl/roundcube");
        driver.manage().window().maximize();
        Thread.sleep(1000);
        driver.findElementById("rcmloginuser").sendKeys(login+"@selenium.waw.pl");
        driver.findElementById("rcmloginpwd").sendKeys(haslo);
        driver.findElementById("rcmloginsubmit").click();

        }

    public void SendMail(ChromeDriver driver,String login) throws InterruptedException {
        for (int i=0; i < 3; i++)
        {
            driver.findElementById("rcmbtn107").click();
            Thread.sleep(1000);
            driver.findElementById("_to").sendKeys(login+"@selenium.waw.pl");
            driver.findElementById("compose-subject").sendKeys("Temat"+i);
            driver.findElementById("composebody").sendKeys("Wiadomosc"+i);
            driver.findElementById("rcmbtn107").click();
            Thread.sleep(3000);
        }
    }


}
