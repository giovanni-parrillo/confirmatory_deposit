from operator import itemgetter

#variables
c = 100 #cost of performance
v = 130 #value of the performance for the buyer
r = 20 #reliance investment of the buyer
w = 10 #value of the reliance investment in case of breach
p = 120 #price of the performance
x = 0.1*p #confirmatory deposit
L = 10 #litigation cost

#payoff defined as ['outcome', payoff_buyer, payoff_seller]
performance_outcome = ['Both perfom', v-r-p, p-c]

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
    print('\n     since ', performance_outcome, '>', sb_preferred, ' the seller is willing to perform')
else:
    seller_choice = 'breach'
    print('\n     since ', performance_outcome, '<', sb_preferred, ' the seller is willing to breach')

#buyer's decision to perform
if performance_outcome[1] > bb_preferred[1]:
    buyer_choice = 'perform'
    print('     since ', performance_outcome, '>', bb_preferred, ' the buyer performs')
else:
    buyer_choice = 'breach'
    print('     since ', performance_outcome, '<', bb_preferred, ' the buyer breaches')


#Nash equilibrium:

if buyer_choice == 'perform':
    if seller_choice == 'perform':
        outcome = performance_outcome
    else:
        outcome = sb_preferred
else:
    outcome = bb_enforced

print('\nThe Nash equilibrium of the  game is ', outcome)
surplus = outcome[1] + outcome[2]
print('The total social surplus is ', surplus,'\n')