package main;

import java.io.BufferedReader;

public class App 
{
    public static void main( String[] args )
    {
        try {
            System.out.println("Welcome to a maven service");
            System.out.println("Press Enter to stop server");
            // wait for Enter to terminate
            new BufferedReader(new java.io.InputStreamReader(System.in)).readLine();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
