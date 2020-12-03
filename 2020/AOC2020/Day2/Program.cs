using System;
using System.IO;
using System.Linq;

namespace Day2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] pwds = File.ReadAllLines(@"C:\data\dotnet_projects\adventofcode\2020\day1\Day2\input_01.txt");
            int pwdCounter = 0;
            foreach(string pwd in pwds)
            {
                if (EvaluatePassword(pwd)) pwdCounter++;
            }
            Console.WriteLine("the number is: " + pwdCounter);
        }

        private static bool EvaluatePassword(string pwd)
        {
            string[] parts = pwd.Split(':');
            string[] rulesParts = parts[0].Split(' ');
            string pwdToEval = parts[1].Trim();

            string[] limits = rulesParts[0].Split('-');
            char letter = rulesParts[1][0];

            int lowerLimit = int.Parse(limits[0]);
            int upperLimit = int.Parse(limits[1]);
            return Eval2(pwdToEval, letter, lowerLimit, upperLimit);
        }

        private static bool Eval2(string pwdToEval, char letter, int lowerLimit, int upperLimit)
        {
            return pwdToEval[lowerLimit - 1] == letter ^ pwdToEval[upperLimit - 1] == letter;
        }

        private static bool Eval1(string pwdToEval, char letter, int lowerLimit, int upperLimit)
        {
            int occurrences = pwdToEval.Count(x => x == letter);

            return (occurrences >= lowerLimit && occurrences <= upperLimit);
        }
    }
}
