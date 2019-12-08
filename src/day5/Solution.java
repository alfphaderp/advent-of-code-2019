package day5;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

import util.IntcodeEmulator;

public class Solution {
	public static void main(String[] args) throws IOException {
		Scanner s = new Scanner(new File("src/day5/input.txt"));
		int[] mem = Arrays.stream(s.nextLine().split(","))
				.mapToInt(Integer::parseInt)
				.toArray();
		s.close();
		
		IntcodeEmulator ie = new IntcodeEmulator(mem);
		ie.run();
	}
}
