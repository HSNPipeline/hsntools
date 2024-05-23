"""I/O related check functions - check file properties."""

###################################################################################################
###################################################################################################

def check_blackrock_file_info(reader):
    """Check some basic information and metadata from a set of Blackrock files.

    Parameters
    ----------
    reader : neo.rawio.blackrockrawio.BlackrockRawIO
        File reader for the Blackrock file(s).
    """

    print('sampling rate: \t', reader.get_signal_sampling_rate())
    print('# channels: \t', reader.signal_channels_count(0))

    n_blocks = reader.block_count()
    for bi in range(n_blocks):
        print('block #{}:'.format(bi))
        n_segments = reader.segment_count(bi)
        for si in range(n_segments):
            print('  seg#{}    start: {:1.2e}    stop:  {:1.2e}\tsize: {:10d}'.format(\
                si, reader.segment_t_start(bi, si), reader.segment_t_stop(bi, si),
                reader.get_signal_size(bi, si)))
