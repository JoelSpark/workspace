#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Beacon Rx
# Generated: Fri Dec 13 18:59:30 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import pmt
import satisfi
import threading
import time

class beacon_rx(gr.top_block):

    def __init__(self, predict_hostname="127.0.0.1", predict_port=1210, uhf_rx_gain=15, control_port=5001, iq_path="/home/nanosatisfi/data/iq/beacon_rx.iq", fwd_to_ip="192.168.0.140", freq_error=0, satellite="39413", uhf_freq=437e6):
        gr.top_block.__init__(self, "Beacon Rx")

        ##################################################
        # Parameters
        ##################################################
        self.predict_hostname = predict_hostname
        self.predict_port = predict_port
        self.uhf_rx_gain = uhf_rx_gain
        self.control_port = control_port
        self.iq_path = iq_path
        self.fwd_to_ip = fwd_to_ip
        self.freq_error = freq_error
        self.satellite = satellite
        self.uhf_freq = uhf_freq

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.doppler_shift = doppler_shift = 0

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", control_port), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        threading.Thread(target=self.xmlrpc_server_0.serve_forever).start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="uhf_usrp_address",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(uhf_freq,10e6), 0)
        self.uhd_usrp_source_0.set_gain(uhf_rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.satisfi_predict_query_0 = satisfi.predict_query(predict_ip=predict_hostname,predict_port=predict_port,sat_name=satellite,freq=uhf_freq,xml_port=control_port,xml_ip="127.0.0.1")
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=96,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 96000)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, iq_path)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(96000, analog.GR_COS_WAVE, -doppler_shift-freq_error, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0_0, "strobe", self.satisfi_predict_query_0, "trig")

# QT sink close method reimplementation

    def get_predict_hostname(self):
        return self.predict_hostname

    def set_predict_hostname(self, predict_hostname):
        self.predict_hostname = predict_hostname

    def get_predict_port(self):
        return self.predict_port

    def set_predict_port(self, predict_port):
        self.predict_port = predict_port

    def get_uhf_rx_gain(self):
        return self.uhf_rx_gain

    def set_uhf_rx_gain(self, uhf_rx_gain):
        self.uhf_rx_gain = uhf_rx_gain
        self.uhd_usrp_source_0.set_gain(self.uhf_rx_gain, 0)

    def get_control_port(self):
        return self.control_port

    def set_control_port(self, control_port):
        self.control_port = control_port

    def get_iq_path(self):
        return self.iq_path

    def set_iq_path(self, iq_path):
        self.iq_path = iq_path
        self.blocks_file_sink_0.open(self.iq_path)

    def get_fwd_to_ip(self):
        return self.fwd_to_ip

    def set_fwd_to_ip(self, fwd_to_ip):
        self.fwd_to_ip = fwd_to_ip

    def get_freq_error(self):
        return self.freq_error

    def set_freq_error(self, freq_error):
        self.freq_error = freq_error
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

    def get_satellite(self):
        return self.satellite

    def set_satellite(self, satellite):
        self.satellite = satellite
        self.satisfi_predict_query_0.set_name(self.satellite)

    def get_uhf_freq(self):
        return self.uhf_freq

    def set_uhf_freq(self, uhf_freq):
        self.uhf_freq = uhf_freq
        self.satisfi_predict_query_0.set_freq(self.uhf_freq)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.uhf_freq,10e6), 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--predict-hostname", dest="predict_hostname", type="string", default="127.0.0.1",
        help="Set predict_hostname [default=%default]")
    parser.add_option("", "--predict-port", dest="predict_port", type="intx", default=1210,
        help="Set predict_port [default=%default]")
    parser.add_option("", "--uhf-rx-gain", dest="uhf_rx_gain", type="eng_float", default=eng_notation.num_to_str(15),
        help="Set uhf_rx_gain [default=%default]")
    parser.add_option("", "--control-port", dest="control_port", type="intx", default=5001,
        help="Set control_port [default=%default]")
    parser.add_option("", "--iq-path", dest="iq_path", type="string", default="/home/nanosatisfi/data/iq/beacon_rx.iq",
        help="Set iq_path [default=%default]")
    parser.add_option("", "--fwd-to-ip", dest="fwd_to_ip", type="string", default="192.168.0.140",
        help="Set fwd_to_ip [default=%default]")
    parser.add_option("", "--freq-error", dest="freq_error", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set freq_error [default=%default]")
    parser.add_option("", "--satellite", dest="satellite", type="string", default="39413",
        help="Set satellite [default=%default]")
    parser.add_option("", "--uhf-freq", dest="uhf_freq", type="eng_float", default=eng_notation.num_to_str(437e6),
        help="Set uhf_freq [default=%default]")
    (options, args) = parser.parse_args()
    tb = beacon_rx(predict_hostname=options.predict_hostname, predict_port=options.predict_port, uhf_rx_gain=options.uhf_rx_gain, control_port=options.control_port, iq_path=options.iq_path, fwd_to_ip=options.fwd_to_ip, freq_error=options.freq_error, satellite=options.satellite, uhf_freq=options.uhf_freq)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

