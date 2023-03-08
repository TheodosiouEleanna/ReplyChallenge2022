with open('input.txt') as f:
    lines = f.readlines()
first_line = lines[0].split()

cur_stamina, max_stamina, max_turns, demons = map(int, first_line)

# Create an empty list to store the demon data
demon_data = []

def sort_demons(demons):
    # Sort demons based on the sum of fragments that can be collected in n turns and after that the amount of mana they recover per round
    demons.sort(key=lambda x: ( x[2]/x[3], sum(x[4:])))
    return demons

# Loop over the remaining lines in the input file and store the demon data in a list of tuples
for i in range(1, demons+1):
    demon_line = lines[i].split()
    demon_stamina, turns_before_recover, stamina_recover = map(int, demon_line[:3])
    #appended index at the beginning of the tuple to preserve it for output
    demon_data.append((i-1,demon_stamina, turns_before_recover, stamina_recover))
    fragments = map(int, demon_line[4:])
    demon_data[i-1] = demon_data[i-1] + tuple(fragments)
    
demon_data = sort_demons(demon_data)

demons_faced = []

for i in range(0, demons): demons_faced.append(-1)
    
fragments = 0
turns = 0
stamina_recovery_turns = 0

for i in range(0, demons):
    demon = demon_data[i]
    demon_stamina = demon[1]
    demon_recover_turns = demon[2]
    demon_recover_stamina = demon[3]
   
    while cur_stamina >= demon_stamina and turns < max_turns:
        if(demons_faced[i] == -1):
        # Fight demon and earn fragments
            cur_stamina -= demon_stamina
            # demons_faced[i] += 1
        fragments += demon[4 + demons_faced[i]]
        turns += 1
        stamina_recovery_turns += 1
        if(demons_faced[i] != -1):
            demons_faced[i] += 1
        # Check if enough turns have passed to recover stamina
        if stamina_recovery_turns == demon_recover_turns:
            cur_stamina = min(cur_stamina + demon_recover_stamina, max_stamina)
            stamina_recovery_turns = 0


print(demon_data, fragments)

