package util;

import java.util.Arrays;
import java.util.Scanner;

public class IntcodeEmulator {
	private int[] mem;
	private int insPtr;
	private Scanner in;
	
	public IntcodeEmulator(int[] m) {
		mem = Arrays.copyOf(m, m.length);
	}
	
	public void set(int index, int value) {
		mem[index] = value;
	}
	
	public int get(int index) {
		return mem[index];
	}
	
	public void run() {
		insPtr = 0;
		in = new Scanner(System.in);
		run:
		while(insPtr < mem.length) {
			switch(mem[insPtr] % 100) {
			case 1:
				add(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2], mem[insPtr + 3]);
				insPtr += 4;
				break;
			case 2:
				mult(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2], mem[insPtr + 3]);
				insPtr += 4;
				break;
			case 3:
				input(mem[insPtr], mem[insPtr + 1]);
				insPtr += 2;
				break;
			case 4:
				output(mem[insPtr], mem[insPtr + 1]);
				insPtr += 2;
				break;
			case 5:
				jumpIfTrue(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2]);
				break;
			case 6:
				jumpIfFalse(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2]);
				break;
			case 7:
				lessThan(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2], mem[insPtr + 3]);
				insPtr += 4;
				break;
			case 8:
				equals(mem[insPtr], mem[insPtr + 1], mem[insPtr + 2], mem[insPtr + 3]);
				insPtr += 4;
				break;
			case 99:
				break run;
			default:
				System.err.println(memDump());
				throw new RuntimeException("Invalid opcode at instruction " + insPtr);
			}
		}
		in.close();
	}
	
	private static int[] getModesFromIns(int ins, int n) {
		int[] modes = new int[n];
		ins /= 100;
		for(int i = 0; i < n; i++) {
			modes[i] = ins % 10;
			ins /= 10;
		}
		return modes;
	}
	
	private void add(int ins, int p0, int p1, int p2) {
		int[] modes = getModesFromIns(ins, 3);
		mem[p2] = (modes[0] == 1 ? p0 : mem[p0]) + (modes[1] == 1 ? p1 : mem[p1]);
	}
	
	private void mult(int ins, int p0, int p1, int p2) {
		int[] modes = getModesFromIns(ins, 3);
		mem[p2] = (modes[0] == 1 ? p0 : mem[p0]) * (modes[1] == 1 ? p1 : mem[p1]);
	}
	
	private void input(int ins, int p0) {
		System.out.print("Input: ");
		mem[p0] = in.nextInt();
	}
	
	private void output(int ins, int p0) {
		int[] modes = getModesFromIns(ins, 1);
		System.out.println("Output: " + (modes[0] == 1 ? p0 : mem[p0]));
	}
	
	private void jumpIfTrue(int ins, int p0, int p1) {
		int[] modes = getModesFromIns(ins, 2);
		if((modes[0] == 1 ? p0 : mem[p0]) != 0)
			insPtr = modes[1] == 1 ? p1 : mem[p1];
		else
			insPtr += 3;
	}
	
	private void jumpIfFalse(int ins, int p0, int p1) {
		int[] modes = getModesFromIns(ins, 2);
		if((modes[0] == 1 ? p0 : mem[p0]) == 0)
			insPtr = modes[1] == 1 ? p1 : mem[p1];
		else
			insPtr += 3;
	}
	
	private void lessThan(int ins, int p0, int p1, int p2) {
		int[] modes = getModesFromIns(ins, 3);
		if((modes[0] == 1 ? p0 : mem[p0]) < (modes[1] == 1 ? p1 : mem[p1]))
			mem[p2] = 1;
		else
			mem[p2] = 0;
	}
	
	private void equals(int ins, int p0, int p1, int p2) {
		int[] modes = getModesFromIns(ins, 3);
		if((modes[0] == 1 ? p0 : mem[p0]) == (modes[1] == 1 ? p1 : mem[p1]))
			mem[p2] = 1;
		else
			mem[p2] = 0;
	}
	
	public String memDump() {
		return Arrays.toString(mem);
	}
}
