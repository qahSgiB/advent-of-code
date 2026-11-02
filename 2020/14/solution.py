from typing import List, Tuple, Dict



def load_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file: return input_file.read()


def parse_mask_command(command: str) -> Tuple[int, int]:
    mask_str = command[7:]

    orrer = 0
    ander = 0

    for mash_char in mask_str:
        if mash_char == 'X':
            orrer = orrer << 1
            ander = (ander << 1) | 1

        elif mash_char == '1':
            orrer = (orrer << 1) | 1
            ander = (ander << 1) | 1

        elif mash_char == '0':
            orrer = orrer << 1
            ander = ander << 1

    return orrer, ander

def parse_mask_floating_command(command: str) -> Tuple[int, int]:
    mask_str = command[7:]

    mask = 0
    floating = 0

    for mash_char in mask_str:
        if mash_char == 'X':
            floating = (floating << 1) | 1
            mask = mask << 1

        elif mash_char == '1':
            floating = (floating << 1)
            mask = mask << 1 | 1

        elif mash_char == '0':
            floating = (floating << 1)
            mask = mask << 1

    return mask, floating

def parse_mem_command(command: str) -> Tuple[int, int]:
    eq_index = command.index('=')

    loc = int(command[4:eq_index-2])
    value = int(command[eq_index+2:])

    return loc, value

def get_command_type(command: str) -> str:
    if command[:4] == 'mask': return 'mask'
    elif command[:3] == 'mem': return 'mem'

    return ''


def input_to_command_strs(inp: str) -> List[str]:
    return inp.split('\n')


def solve_b(inp: str) -> int:
    command_strs = input_to_command_strs(inp)

    active_mask = 0
    active_floating_poss: List[int] = []
    memory: Dict[int, int] = {}

    for command_str in command_strs:
        command_type = get_command_type(command_str)

        if command_type == 'mask':
            active_mask, floating = parse_mask_floating_command(command_str)

            active_floating_poss.clear()

            bit = 0
            while floating != 0:
                if floating & 1 == 1: active_floating_poss.append(bit)

                floating >>= 1
                bit += 1

        elif command_type == 'mem':
            base_loc, value = parse_mem_command(command_str)
            base_loc |= active_mask

            for floating_bits in range(2**len(active_floating_poss)):
                loc = base_loc

                for index, floating_pos in enumerate(active_floating_poss):
                    if (floating_bits >> index) & 1 == 1: loc |= 1 << floating_pos
                    else:                                 loc &= ~(1 << floating_pos)

                memory[loc] = value

    memory_sum = 0
    for loc in memory: memory_sum += memory[loc]

    return memory_sum



input_ = load_input('input.txt')
test_input = load_input('test_input1.txt')