#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Log IQ From UDP
# Author: Joel Spark
# Generated: Fri Oct 18 02:11:13 2013
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time

class log_iq_udprx(gr.top_block):

    def __init__(self, sat="noname"):
        gr.top_block.__init__(self, "Log IQ From UDP")

        ##################################################
        # Parameters
        ##################################################
        self.sat = sat

        ##################################################
        # Variables
        ##################################################
        self.timestamp = timestamp =  str(time.gmtime().tm_year) + time.strftime("%m%d-%H%M",time.gmtime())
        self.samp_rate = samp_rate = 40000
        self.iq_filename = iq_filename = '/home/jspark/data/iq/' + timestamp + '-' + sat

        ##################################################
        # Blocks
        ##################################################
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, "192.168.0.200", 8888, 32768, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, iq_filename)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))


# QT sink close method reimplementation

    def get_sat(self):
        return self.sat

    def set_sat(self, sat):
        self.sat = sat
        self.set_iq_filename('/home/jspark/data/iq/' + self.timestamp + '-' + self.sat)

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        self.set_iq_filename('/home/jspark/data/iq/' + self.timestamp + '-' + self.sat)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_iq_filename(self):
        return self.iq_filename

    def set_iq_filename(self, iq_filename):
        self.iq_filename = iq_filename
        self.blocks_file_sink_0.open(self.iq_filename)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--sat", dest="sat", type="string", default="noname",
        help="Set sat [default=%default]")
    (options, args) = parser.parse_args()
    tb = log_iq_udprx(sat=options.sat)
    tb.start()
    tb.wait()

