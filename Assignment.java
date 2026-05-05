// calculator

package Programz;

import java.util.Scanner;

public class Assignment {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Calculator calculator = new Calculator();
		boolean flag = true;
		String history = "";
		double result,a,b;
		String ui;
		while (flag) {
			while (true) {
				System.out.print("Please enter the first number: ");
				ui=input.next();
				try {
					a = Double.parseDouble(ui);
					break;
				} catch (NumberFormatException e) {
					System.out.println("Invalid Input");
				}
			}
			while (true) {
				System.out.print("Please enter the second number: ");
				ui=input.next();
				try {
					b = Double.parseDouble(ui);
					break;
				} catch (NumberFormatException e) {
					System.out.println("Invalid Input");
				}
			}
			
		
			System.out.println("Select operation:\r\n"
					+ "1. Addition\r\n"
					+ "2. Subtraction\r\n"
					+ "3. Multiplication\r\n"
					+ "4. Division\r\n"
					+ "5. Exponentiation\r\n"
					+ "6. Remainder ");
			System.out.print("Enter your choice: ");
			int operator = input.nextInt();
			System.out.println();
			switch (operator) {
			case 1:
				result = calculator.add(a, b);
				System.out.println("Result: " + result);
				history+= Double.toString(a) + " + " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
				break;
			
			case 2:
				result = calculator.sub(a, b);
				System.out.println("Result: " + result);
				history+= Double.toString(a) + " - " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
				break;
			
			case 3:
				result = calculator.multiply(a, b);
				System.out.println("Result: " + result);
				history+= Double.toString(a) + " * " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
				break;
			case 4:
				if (b!=0) {
					result = calculator.divide(a, b);
					System.out.println("Result: " + result);
					history+= Double.toString(a) + " / " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
					break;
				}
				else {
					System.out.println("Error: Cannot divide by zero! ");
					break;
				}
			case 5:
				result = calculator.exp(a, b);
				System.out.println("Result: " + result);
				history+= Double.toString(a) + " ^ " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
				break;
			case 6:
				result = calculator.rem(a, b);
				System.out.println("Result: " + result);
				history+= Double.toString(a) + " % " + Double.toString(b) + " = " + Double.toString(result) + "\r\n";
				break;
			}
			System.out.println();	
			cc: while (true) {
				System.out.print("Do you want to perform another calculation? (Y/N): ");
				String user = input.next();
				if ((user.charAt(0)=='Y')|| (user.charAt(0)=='y')) {
					flag=true;
					break cc;
				}
				else if ((user.charAt(0)=='N')|| (user.charAt(0)=='n')) {
					flag = false;
					aa: while (true) {
						System.out.println("Want to see Calculator history?: ");
						String user1 = input.next();
						if ((user1.charAt(0)=='Y')|| (user1.charAt(0)=='y')) {
							System.out.println(history);
							break aa;
						}
						else if ((user1.charAt(0)=='N')|| (user1.charAt(0)=='n')) {
							flag = false;
							break aa;
						}
						else {
							System.out.println("Invalid Input");
						}
					}
					break cc;
				}
				else {
					System.out.println("Invalid Input");
				}
			}

			
			
		}
	}
}

class Calculator {
	public double add(double a, double b) {
		return a+b;
	}
	public double sub(double a, double b) {
		return a-b;
	}
	public double multiply(double a, double b) {
		return a*b;
	}
	public double divide(double a, double b) {
		return a/b;
	}
	public double exp(double a, double b) {
		return Math.pow(a, b);
	}
	public double rem(double a, double b) {
		return a%b;
	}	
}
