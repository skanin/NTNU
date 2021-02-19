package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

/**
 * @author Sander Lindberg
 * Rules:
 * 	(Basic Farkle rules, the way I understood them xD)
 * 
 * 	If the player only has thrown the dies once:
 * 		Each 1 : 100 score
 * 		Each 5 : 50 score
 * 		Three 1s : 1000 points
 * 		Three of the rest : face * 100. Example three 2s = 2*100.
 * 
 * 	If the player has more than one throw:
 * 		Each 1 : 100 score
 * 		Each 5 : 50 score
 * 		Three 1s: number of ones * 100.
 * 		Three 5s: number of fives * 100.
 * 		Three of the rest : face * 100. Example three 2s = 2*100.
 * 
 * 	To lazy/unexperienced to implement three pair/Straight/house etc..
 * 	Not sure if hot dice works :p 
 * 
 * 	To play: Run this file (Game.java) and follow the instructions. 
 */

public class Game {
	private static final int WINNING_SCORE = 10000;
	private List<Player> players;
	private List<Dice> dies;
	private List<Dice> validRolls;
	private List<Dice> setAside;
	private Scanner sc;
	private Player currentPlayer;
	private int ones, twos, threes, fours, fives, sixes;
	
	public Game(Player...players) {
		this.players = new ArrayList<Player>(Arrays.asList(players));
		setDies();
		this.setAside = new ArrayList<Dice>();
		this.validRolls = new ArrayList<Dice>();
		this.sc = new Scanner(System.in);
	}
	
	
	//Checks if there is a winner
	public boolean hasWinner() {
		return players.stream().anyMatch(p -> p.getScore() >= WINNING_SCORE);
	}
	
	//Sets the dies 0-5
	public void setDies() {
		Dice d0 = new Dice();
		Dice d1 = new Dice();
		Dice d2 = new Dice();
		Dice d3 = new Dice();
		Dice d4 = new Dice();
		Dice d5 = new Dice();
		this.dies = new ArrayList<Dice>(Arrays.asList(d0, d1, d2, d3, d4, d5));
	}
	
	public void setValidRolls() {
		List<Integer> faces = new ArrayList<Integer>();
		for(Dice d : dies) {
			faces.add(d.getFace());
		}
		
		validRolls = dies.stream().filter(p -> (p.isValidRoll() && !p.getIsSetAside()) || (Collections.frequency(faces, p.getFace()) == 3))
				.collect(Collectors.toList());
	}
	
	//Sets the current player
	public void setCurrentPlayer(Player p) {
		this.currentPlayer = p;
	}
	
	//Adds a player
	public void addPlayer(Player p) {
		players.add(p);
	}
	
	//Sets ones, twos, threes, fours, fives, sixes
	public void setFrequency() {
		List<Integer> faces = new ArrayList<Integer>();
		for(Dice d : setAside) {
			faces.add(d.getFace());
		}
		
		this.ones = Collections.frequency(faces, 1);
		this.twos = Collections.frequency(faces, 2);
		this.threes = Collections.frequency(faces, 3);
		this.fours = Collections.frequency(faces, 4);
		this.fives = Collections.frequency(faces, 5);
		this.sixes = Collections.frequency(faces, 6);
	}
	
	//Checks for score and adds this to the current player.
	public void checkForScore() {
		
		int tempScore = 0;
		setFrequency();
		
		if(currentPlayer.getNumberOfThrows() == 1) {
			if(ones == 3) {
				tempScore += 1000;
			}else {
				tempScore += 100*ones;
			}
			if(twos == 3) {
				tempScore += 200;
			}
			if(threes == 3) {
				tempScore += 300;
			}
			if(fours == 3) {
				tempScore += 400;
			}
			if(fives == 3) {
				tempScore += 500;
			}else {
				tempScore += 50*fives;
			}
			if(sixes == 3) {
				tempScore += 600;
			}
		}else {
			tempScore += (100*ones) + (50*fives);
			if(twos == 3) {
				tempScore += 200;
			}
			if(threes == 3) {
				tempScore += 300;
			}
			if(fours == 3) {
				tempScore += 400;
			}
			if(sixes == 3) {
				tempScore += 600;
			}
		}
		currentPlayer.addScore(tempScore);
	}
	
	//Checks for farkle
	public boolean checkFarkle() {
		return validRolls.isEmpty();
	}
	
	//Checks for hot dice and adds score
	public boolean checkHotDice() {
		if((validRolls.size() + setAside.size() == 6) || validRolls.size() == 6) {
			checkForScore();
			return true;
		}
		return false;
	}
	
	//Prints the current score
	public void printCurrentScore() {
		System.out.println("The score is: ");
		for(Player p : players) {
			System.out.println(p + ": " + p.getScore());
		}
	}
	
	//Rolls all dies
	public void rollAll() {
		setDies();
		dies.stream().forEach(d -> d.roll());
		int i = 1;
		for(Dice d : dies) {
			System.out.println("Dice " + i + " rolls: " + d.getFace());
			i++;
		}
		setValidRolls();
		currentPlayer.incrementNumberOfThrows();
	}
	
	//Rolls the dies that are not sat aside
	public void rollNotSetAside() {
		dies.stream().forEach(d -> {
			if(!d.getIsSetAside()) d.roll();
		});
		int i = 1;
		for(Dice d : dies) {
			System.out.println("Dice " + i + " rolls: " + d.getFace());
			i++;
		}
		
		List<Integer> faces = new ArrayList<Integer>();
		for(Dice d : dies) {
			faces.add(d.getFace());
		}
		setValidRolls();
		currentPlayer.incrementNumberOfThrows();
	}
	
	//Changes the player based on ID. 1 goes first, then changes to 2, to 3 etc.. And back to 1
	public void changePlayer() {
		currentPlayer.setNumberOfThrows(0);
		if(currentPlayer.getId() == Player.COUNTER - 1) {
			printCurrentScore();
			currentPlayer = players.stream().filter(p -> p.getId() == 0).findAny().get();
		}else {
			currentPlayer = players.stream().filter(p -> p.getId() == currentPlayer.getId() + 1).findAny().orElse(null);
		}
	}
	
	//Returns the current player
	public Player getCurrentPlayer() {
		return this.currentPlayer;
	}
	
	//Asks for players and adds them based on input and sets the current player
	public void init() {
		
		if (players.isEmpty()) {
			System.out.println("How many players? ");
			int playerCount = sc.nextInt();
			System.out.println();
			int i = 1;
			while (players.size() != playerCount) {
				System.out.println("Player " + i + "'s name: ");
				sc = new Scanner(System.in);
				String playerName = sc.nextLine();
				addPlayer(new Player(playerName));
				i++;
			} 
		}
		currentPlayer = players.stream().filter(p -> p.getId() == 0).findAny().orElse(null);
		System.out.println(currentPlayer + " starts!");
		
	}
	
	//Runs while the game does not have a winner. This is the method that actually "plays" the game
	public void play() {
		while(!hasWinner()) {
			System.out.println();
			System.out.println(getCurrentPlayer() + "'s turn");
			System.out.println("Type 'Roll all' to roll all: ");
			sc = new Scanner(System.in);
			String inp = sc.nextLine();
			
			while (!inp.equals("Roll all")) {
				System.out.println("Type 'Roll all' to roll all: ");
				sc = new Scanner(System.in);
				inp = sc.nextLine();
			}
			
			if (inp.equals("Roll all")) {
				rollAll();
				if(checkHotDice()) {
					System.out.println("HOLY SHIT, YOU GOT A HOT DICE, U KNOW WHAT THAT MEANS??? YOU CAN THROW ALL THE DIES AGAIN, ADDING TO THE SCORE FOR THE DIES YOU'VE ALREADY THROWN!!!! GG MAN");
					break;
				}else if(checkFarkle()) {
					System.out.println("You farkled! All points are lost");
					setAside = new ArrayList<Dice>();
					changePlayer();
					continue;
				}
			} 
				String ans = "N";
				
				while(ans.equals("N")) {
					if(!validRolls.isEmpty()) {
						System.out.println("\nYou must set aside one or more of the following: ");
						
						for(Dice d : validRolls) {
							System.out.println("Dice " + (dies.indexOf(d) + 1));
						}
						
						
						boolean valid = false;
						while(!valid) {
							System.out.println("Which one/ones do you want to set aside (separate using ';')? ");
							sc = new Scanner(System.in);
							String[] aside = sc.nextLine().split(";");
							
							List<Dice> tempList = new ArrayList<Dice>();
							List<Integer> tempListInt = new ArrayList<Integer>();
							for(String s : aside) {
								tempListInt.add(dies.get(Integer.parseInt(s)-1).getFace());
							}
							asideLoop : for(String s : aside) {
								if((dies.get(Integer.parseInt(s)-1).getFace() == 5 || dies.get(Integer.parseInt(s)-1).getFace() == 1)
										|| (Collections.frequency(tempListInt, (dies.get(Integer.parseInt(s)-1)).getFace()) == 3)) {
									if(!tempList.contains(dies.get(Integer.parseInt(s) - 1))) {
										tempList.add(dies.get(Integer.parseInt(s) - 1)); 
									}
									valid = true;
								}else {
									System.out.println("Dice " + s + " can't be sat aside");
									System.out.println("Face: " + dies.get(Integer.parseInt(s)-1).getFace());
									System.out.println(Collections.frequency(dies, (dies.get(Integer.parseInt(s)-1)).getFace()) == 3);
									valid = false;
									continue asideLoop;
								}
							}
							
							
							if(valid == true) {
								tempList.stream().forEach(p -> setAside.add(p));
								int j = 1;
								System.out.println("You sat aside ");
								for(String s : aside) {
									System.out.println("Dice " + s + " ");
									dies.remove(Integer.parseInt(s) - j);
									j++;
								}
							}
							
						}
						
						validRolls = new ArrayList<Dice>();
						System.out.println("\nDo you want to end your turn (Y/N)? ");
						sc = new Scanner(System.in);
						ans = sc.nextLine();
					}else {
						System.out.println("If you changed your mind and want to end your turn, type 'Y', else, type 'Roll' to"
								+ " roll your remaining dies");
						sc = new Scanner(System.in);
						String endTurn = sc.nextLine();
						if(endTurn.equals("Y")){
							checkForScore();
							validRolls = new ArrayList<Dice>();
							break;
						}else if(endTurn.equals("Roll")) {
							rollNotSetAside();
							if(checkFarkle()) {
								System.out.println("You farkled! All points are lost");
								setAside = new ArrayList<Dice>();
								break;
							}else if(checkHotDice()) {
								System.out.println("HOLY SHIT, YOU GOT A HOT DICE, U KNOW WHAT THAT MEANS??? YOU CAN THROW ALL THE DIES AGAIN, ADDING TO THE SCORE FOR THE DIES YOU'VE ALREADY THROWN!!!! GG MAN");
								break;
							}
						}
					}
				}
				if(!checkHotDice()) {
					checkForScore();
					setAside = new ArrayList<Dice>();
					changePlayer();
				}else {
					getCurrentPlayer().setNumberOfThrows(0);
				}
				
			}
			System.out.println("The winner is: " + players.stream().filter(p -> p.getScore() >= WINNING_SCORE).findFirst().get());
			
		}
	
	//Main method to play the game
	public static void main(String[] args) {
		Game g = new Game();
		g.init();
		g.play();
	}
}
