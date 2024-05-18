from operator import itemgetter
import random as rd
import pandas as pd

results=[['outcome', 'B', 'S']]
results_surplus=['surplus']
variables=[['c', 'v', 'r', 'w', 'p', 'x', 'L']]
social_surplus = [['social best', 'optimum surplus', 'efficiency']]

rd.seed(5) 

for i in range(0, 100000):

    #variables 
    v = rd.randint(1,100) #value of the performance for the buyer
    r = rd.randint(1,100) #reliance investment of the buyer
    w = r/rd.randint(1,4) #value of the reliance investment in case of breach
    p = rd.randint(1,100) #price of the performance
    c = rd.randint(1,100) #cost of performance
    x = p*rd.randint(1,99)/100 #confirmatory deposit
    L = rd.randint(1,100) #litigation cost

    variables.append([c,v,r,w,p,x,L])

    #payoff defined as ['outcome', payoff_buyer, payoff_seller]
    performance_outcome = ['Both perform', v-r-p, p-c]

    #seller breaches
    sb_deposit = ['Seller\'s breach - deposit remedy', w-r+x, -x]
    sb_enforced = ['Seller\'s breach - enforced performance', v-r-p, p-c-L]
    sb_judicial = ['Seller\'s breach - judicial remedy', 0, w-r-L]

    #buyer breaches
    bb_deposit = ['Buyer\'s breach - deposit remedy', w-r-x, x]
    bb_enforced = ['Buyer\'s breach - enforced performance', v-r-p-L, p-c]
    bb_judicial = ['Buyer\'s breach - judicial remedy', -L, 0]

    complete_payoffs = [performance_outcome,
                        sb_deposit, sb_enforced, sb_judicial,
                        bb_deposit, bb_enforced, bb_judicial]

    #print(complete_payoffs)

    #Computing Nash equilibrium with backwards induction

    #seller breaches, buyer chooses remedy
    sb_complete = [sb_deposit, sb_enforced, sb_judicial]
    sb_sorted = sorted(sb_complete, key=itemgetter(1))
    sb_preferred = sb_sorted[-1]
    #print('If the seller breaches, the buyer chooses ', sb_preferred[0])



    #buyer breaches, seller chooses remedy
    bb_complete = [bb_deposit, bb_enforced, bb_judicial]
    bb_sorted = sorted(bb_complete, key=itemgetter(2))
    bb_preferred = bb_sorted[-1]
    #print('If the buyer breaches, the seller chooses ', bb_preferred[0])

    #seller's decision once buyer has performed
    if performance_outcome[2] > sb_preferred[2]:
        seller_choice = 'perform'
    else:
        seller_choice = 'breach'

    #buyer's decision to perform
    if performance_outcome[1] > bb_preferred[1]:
        buyer_choice = 'perform'
    else:
        buyer_choice = 'breach'


    #Nash equilibrium:

    if buyer_choice == 'perform':
        if seller_choice == 'perform':
            outcome = performance_outcome
        else:
            outcome = sb_preferred
    else:
        outcome = bb_enforced

    #print('The Nash equilibrium of the  game is ', outcome)
    surplus = outcome[1] + outcome[2]
    #print('The total social surplus is ', surplus)

    results.append(outcome)
    results_surplus.append(surplus)

    social_complete =[]

    for x in complete_payoffs:
        value = x[1]+x[2]
        social_complete.append([x[0],value])

    social_sorted = sorted(social_complete, key=itemgetter(1))
    social_best = social_sorted[-1]

    if social_best[0]==outcome[0]:
        eff = 1
    else:
        eff = 0
    social_best.append(eff)
    social_surplus.append(social_best)


df = pd.DataFrame(results)
df1 = pd.DataFrame(variables)
df2 =pd.DataFrame(results_surplus)
df3 = pd.DataFrame(social_surplus)


dati = pd.concat([df, df1, df2, df3], axis=1)

# saving the dataframe
dati.to_csv('simulation_results.csv')


