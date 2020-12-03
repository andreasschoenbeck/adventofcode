using System;
using System.IO;

namespace Day3
{
    class Program
    {

        static string[] slopePart = null;
        static int width = 0;
        static void Main(string[] args)
        {
            slopePart = File.ReadAllLines(@"C:\data\dotnet_projects\adventofcode\2020\day1\Day3\input_01.txt");
            width = slopePart[0].Length;

            int row = 0;
            int col = 0;
            //Part1(ref row, ref col);
            Part2(ref row, ref col);

        }

        private static void Part2(ref int row, ref int col)
        {
            int treeCounter1 = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter1++;
                row += 1;
                col += 1;
            }

            row = 0;
            col = 0;
            int treeCounter2 = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter2++;
                row += 1;
                col += 3;
            }

            row = 0;
            col = 0;
            int treeCounter3 = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter3++;
                row += 1;
                col += 5;
            }

            row = 0;
            col = 0;
            int treeCounter4 = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter4++;
                row += 1;
                col += 7;
            }

            row = 0;
            col = 0;
            int treeCounter5 = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter5++;
                row += 2;
                col += 1;
            }
            Console.WriteLine("Trees: " + (treeCounter1 * treeCounter2 * treeCounter3 * treeCounter4 * treeCounter5));
        }

        private static void Part1(ref int row, ref int col)
        {
            int treeCounter = 0;
            while (row < slopePart.Length)
            {
                if (CheckTreeAt(col, row)) treeCounter++;
                row += 1;
                col += 3;
            }

            Console.WriteLine("Trees: " + treeCounter);
        }

        static bool CheckTreeAt(int col, int row)
        {
            return (slopePart[row][col % width] == '#');
        }
    }
}
