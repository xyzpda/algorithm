// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
var result = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
Console.WriteLine(result[0]);
Console.WriteLine(result[1]);
