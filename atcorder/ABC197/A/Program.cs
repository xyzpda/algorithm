using System;

class A
{
    static void Main(string[] args)
    {
        var result = Console.ReadLine();
        Console.WriteLine(result[1].ToString() + result[2].ToString() + result[0].ToString());
    }
}