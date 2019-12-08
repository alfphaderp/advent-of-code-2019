package day2;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

import util.IntcodeEmulator;

public class Solution {
	public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(new File("src/day2/input.txt"));
		int[] mem = Arrays.stream(s.nextLine().split(","))
				.mapToInt(Integer::parseInt)
				.toArray();
		s.close();
		
		System.out.println(part1(mem, 12, 2));
		System.out.println(part2(mem));
	}
	
	public static int part1(int[] mem, int a, int b) {
		IntcodeEmulator ie = new IntcodeEmulator(mem);
		ie.set(1, a);
		ie.set(2, b);
		ie.run();
		return ie.get(0);
	}

	public static String part2(int[] mem) {
		for(int i = 0; i <= 99; i++)
			for(int j = 0; j <= 99; j++) {
				if(part1(mem, i, j) == 19690720)
					return i + "" + j;
			}
		
		throw new RuntimeException("Valid input pair not found");
	}
}
