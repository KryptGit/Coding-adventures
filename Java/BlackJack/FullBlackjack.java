
//Name: 
import java.io.Console;
import java.util.*;
import java.util.ArrayList;
import java.util.List;
public class FullBlackjack
{

    public static void main(String[] args)
    {
        Scanner console = new Scanner(System.in);
        Deck deck = new Deck();
        boolean loop = true;
        System.out.println("  ____    _                  _           _                  _   ");
        System.out.println(" |  _ \\  | |                | |         | |                | |");
        System.out.println(" | |_) | | |   __ _    ___  | | __      | |   __ _    ___  | | __");
        System.out.println(" |  _ <  | |  / _` |  / __| | |/ /  _   | |  / _` |  / __| | |/ /");
        System.out.println(" | |_) | | | | (_| | | (__  |   <  | |__| | | (_| | | (__  |   < ");
        System.out.println(" |____/  |_|  \\__,_|  \\___| |_|\\_\\  \\____/   \\__,_|  \\___| |_|\\_\\\n\n\n");
        while (loop)
        {
            int playerHand = 0;
            int DealerHand = 0;
            DealerHand += deck.dealCard();
            DealerHand += deck.dealCard();
            playerHand += deck.dealCard();
            playerHand += deck.dealCard();
            display(playerHand, DealerHand, true);
            boolean pTurn = true;
            boolean dTurn = true;
            while (pTurn)
            {
                System.out.print("Do you want to hit?(true or false) ------> ");
                if (console.nextBoolean())
                {
                    playerHand += deck.dealCard();
                    display(playerHand, DealerHand, true);
                    if (playerHand > 21 )
                    {
                        System.out.println("Dang... You Busted!");
                        pTurn = false;
                        
                    }
                }
                else
                {
                    pTurn = false;    
                }

            }
            while (dTurn)
            {
                
                if(DealerHand < 15)
                {
                    DealerHand += deck.dealCard();

                }
                else 
                {
                    display(playerHand, DealerHand, false);
                    dTurn = false;

                } 





            }

            if (playerHand > 21)
            {
                playerHand = -1;
            }
            if (DealerHand > 21)
            {
                DealerHand = -1;
            }

            if (DealerHand > playerHand && DealerHand > 0)
            {
                System.out.println("dealer won");
            } 
            else if (playerHand > DealerHand && playerHand > 0)
            {
                System.out.println("player won");
            }
            else{System.out.println("Draw");}

            System.out.print("Wanna Play again");
            loop = console.nextBoolean();
            
        }


        
    }

    public static void clear()
    {
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }

    public static void display(int p  , int d, Boolean hide)
    {
        if (hide)
        {
            System.out.println("Your Hand ---------> "+ p);
            System.out.println("Dealer ---------> ▋▋▋▋▋▋");


        }
        else 
        {
            System.out.println("Your Hand ---------> "+ p);
            System.out.println("Dealer ---------> " + d);
        }



    }

    
    

}

class Deck {
    ArrayList<Integer> deck = new ArrayList<Integer>(Arrays.asList(2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11));
    public int dealCard()
    {
      
      Random randomGen = new Random();
      int i;
      i = randomGen.nextInt(deck.size());
      int card = deck.get(i);
      deck.remove(i);
      return card;
    }


}
