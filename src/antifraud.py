import sys, csv, io
from helper_methods import replace_esc_chars


if __name__ == '__main__':
    # Additional feature: this program can take any DEGREE > 0
    DEGREE = int(sys.argv[1])

    # Delete old output from the output file
    with open(sys.argv[4], 'w') as output_file:
        output_file.write('')

    # Load training data from the batch input file
    with open(sys.argv[2], 'r') as batch_input_file:
        batch_input_reader = csv.DictReader(io.StringIO(replace_esc_chars(batch_input_file.read()),
                                                        newline=None),
                                            quoting=csv.QUOTE_NONE,
                                            skipinitialspace=True)

    # Load testing data from the stream input file
    with open(sys.argv[3], 'r') as stream_input_file:
        stream_input_reader = csv.DictReader(io.StringIO(replace_esc_chars(stream_input_file.read()),
                                                         newline=None),
                                             quoting=csv.QUOTE_NONE,
                                             skipinitialspace=True)


    output_file = open(sys.argv[4], 'a')

    if DEGREE <= 0:
        # Assume no such case since the coding challenge did not mention it.
        pass
    else:
        if DEGREE == 1 or DEGREE == 2:
            from degree_1_and_2_solution import build_graph_network
            from degree_1_and_2_solution import verifier
        else: # DEGREE > 1
            from general_solution import build_graph_network
            from general_solution import verifier
        graph = build_graph_network(batch_input_reader)
        verifier(stream_input_reader, graph, DEGREE, output_file)

    output_file.close()
