using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] numbers = File.ReadAllLines(@"C:\data\dotnet_projects\adventofcode\2020\day1\ConsoleApp1\input_01.txt");
            int[] integers = numbers.Select(x => int.Parse(x)).ToArray();

            int n1 = 0;
            int n2 = 0;
            int n3 = 0;
            for (int i = 0; i<integers.Length; i++)
            {
                n1 = integers[i];
                for(int j = i+1; j < integers.Length; j++)
                {
                    n2 = integers[j];
                    for (int k = j + 1; k < integers.Length; k++)
                    {
                        n3 = integers[k];
                        if ((n1 + n2 + n3) == 2020)
                        {
                            Console.WriteLine("number is: " + (n1 * n2 * n3));
                            break;
                        }
                    }
                }
            }

            
        }
    }
}
