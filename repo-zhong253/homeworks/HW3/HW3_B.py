#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:59:46 2019

@author: shanshanzhong
"""
# CSCI1133,Lab Section 004,HW3 Shanshan Zhong,Problem3B
       
def main():
    for i in range(1,4):
        print('Game %s: ' % i)
        player_1 = input('Rock...Paper...Scissors! Player 1 (R/P/S): ')
        print('Player 1: ', player_1)
        player_2 = input('Rock...Paper...Scissors! Player 2 (R/P/S): ')
        print('Player 2: ', player_2)
        result = rock_paper_scissors(player_1,player_2)
    ply_1 = result[0]
    ply_2 = result[1]
    if ply_1 == ply_2:
        print("Final Determination: It is a Tie! No one won this round.")
    elif ply_1 > ply_2:
        print("Final Determination: Player 1 won this round.")
    elif ply_2 > ply_1:
        print("Final Determination: Player 2 won this round.")
        
        
def rock_paper_scissors(player_1,player_2):
    pl_1 = 0
    pl_2 = 0
    if player_1 == player_2:
        print("It's a tie, nobody wins.")
        pl_1 += 0
        pl_2 += 0
    elif (player_1 == 'R') and (player_2 == 'P'):
        print("Player 2 Wins!")
        pl_1 += 0
        pl_2 += 1
    elif (player_1 == 'P') and (player_2 == 'R'):
        print("Player 1 Wins!")
        pl_1 += 1
        pl_2 += 0
    elif (player_1 == 'R') and (player_2 == 'S'):
        print("Player 1 Wins!")
        pl_1 += 1
        pl_2 += 0
    elif (player_1 == 'S') and (player_2 == 'R'):
        print("Player 2 Wins!")
        pl_1 += 0
        pl_2 += 1
    elif (player_1 == 'P') and (player_2 == 'S'):
        print("Player 2 Wins!")
        pl_1 += 0
        pl_2 += 1
    elif (player_1 == 'S') and (player_2 == 'P'):
        print("Player 1 Wins!")
        pl_1 += 1
        pl_2 += 0
    return pl_1, pl_2
 
rock_paper_scissors(2,1)
    
main()