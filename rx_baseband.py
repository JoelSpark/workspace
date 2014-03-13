#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Rx Baseband
# Generated: Thu Mar 13 13:37:36 2014
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time

class rx_baseband(gr.top_block):

    def __init__(self, minutes=5, freq=401.525e6, samp_rate=2e6, filename=""):
        gr.top_block.__init__(self, "Rx Baseband")

        ##################################################
        # Parameters
        ##################################################
        self.minutes = minutes
        self.freq = freq
        self.samp_rate = samp_rate
        self.filename = filename

        ##################################################
        # Variables
        ##################################################
        self.max_items = max_items = int(samp_rate*60*minutes)

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, max_items)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, filename, False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))


# QT sink close method reimplementation

    def get_minutes(self):
        return self.minutes

    def set_minutes(self, minutes):
        self.minutes = minutes
        self.set_max_items(int(self.samp_rate*60*self.minutes))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_max_items(int(self.samp_rate*60*self.minutes))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)

    def get_max_items(self):
        return self.max_items

    def set_max_items(self, max_items):
        self.max_items = max_items

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--minutes", dest="minutes", type="eng_float", default=eng_notation.num_to_str(5),
        help="Set minutes [default=%default]")
    parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(401.525e6),
        help="Set freq [default=%default]")
    parser.add_option("", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2e6),
        help="Set samp_rate [default=%default]")
    parser.add_option("", "--filename", dest="filename", type="string", default="",
        help="Set Destination File Name [default=%default]")
    (options, args) = parser.parse_args()
    tb = rx_baseband(minutes=options.minutes, freq=options.freq, samp_rate=options.samp_rate, filename=options.filename)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

