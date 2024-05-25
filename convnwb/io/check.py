"""I/O related check functions - check file properties."""

from convnwb.timestamps.utils import convert_samples_to_time

###################################################################################################
###################################################################################################

def check_blackrock_file_info(reader):
    """Check some basic information and metadata from a set of Blackrock files.

    Parameters
    ----------
    reader : neo.rawio.blackrockrawio.BlackrockRawIO
        File reader for the Blackrock file(s).
    """

    str_fmt = '  seg#{}    start: {:1.2e}    stop: {:1.2e}    size: {:10d}    tlen: {:4.2f}'

    fs = reader.get_signal_sampling_rate()
    n_chans = reader.signal_channels_count(0)

    print('sampling rate: \t', fs)
    print('# channels: \t', n_chans)

    n_blocks = reader.block_count()
    for bi in range(n_blocks):
        print('block #{}:'.format(bi))
        n_segments = reader.segment_count(bi)
        for si in range(n_segments):
            seg_start = reader.segment_t_start(bi, si)
            seg_end = reader.segment_t_stop(bi, si)
            seg_size = reader.get_signal_size(bi, si)
            seg_length = convert_samples_to_time(seg_size, fs)
            print(str_fmt.format(si, seg_start, seg_stop, seg_size, seg_len))
