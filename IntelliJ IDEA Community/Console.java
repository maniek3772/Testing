package com.Selenium;

public class Console
{
    String hello = "I'll be back!";

    public void MethodIf()
    {
        //Skrót: sout + TAB
        System.out.println(hello);

        int zmienna = -1;

        if(zmienna == 0)
        {
            System.out.println("If: " + zmienna);
        }
        else if(zmienna > 0)
        {
            System.out.println("Else If :"+zmienna);
        }
        else {
            System.out.println("Else: " + zmienna);
        }
        System.out.println("Koniec funkcji If");
    }

    public void MethodFor()
    {
        for (int i=0; i < 3; i++)
        {
            System.out.println("For: " + i);
        }
        System.out.println("Koniec funkcji For");
    }
}
