#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Rx Baseband
# Generated: Wed Mar 12 17:32:16 2014
##################################################

execfile("/home/jspark/.grc_gnuradio/size_limited_file_sink_c.py")
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time

class rx_baseband(gr.top_block):

    def __init__(self, minutes=5, freq=401.525e6, filename="", samp_rate=2e6):
        gr.top_block.__init__(self, "Rx Baseband")

        ##################################################
        # Parameters
        ##################################################
        self.minutes = minutes
        self.freq = freq
        self.filename = filename
        self.samp_rate = samp_rate

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
        self.size_limited_file_sink_c_0 = size_limited_file_sink_c(
            file_name=filename,
            max_time=minutes,
            samp_rate=samp_rate,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.size_limited_file_sink_c_0, 0))


# QT sink close method reimplementation

    def get_minutes(self):
        return self.minutes

    def set_minutes(self, minutes):
        self.minutes = minutes
        self.size_limited_file_sink_c_0.set_max_time(self.minutes)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.size_limited_file_sink_c_0.set_file_name(self.filename)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.size_limited_file_sink_c_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--minutes", dest="minutes", type="eng_float", default=eng_notation.num_to_str(5),
        help="Set minutes [default=%default]")
    parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(401.525e6),
        help="Set freq [default=%default]")
    parser.add_option("", "--filename", dest="filename", type="string", default="",
        help="Set filename [default=%default]")
    parser.add_option("", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2e6),
        help="Set samp_rate [default=%default]")
    (options, args) = parser.parse_args()
    tb = rx_baseband(minutes=options.minutes, freq=options.freq, filename=options.filename, samp_rate=options.samp_rate)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

