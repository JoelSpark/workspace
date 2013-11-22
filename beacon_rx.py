#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Beacon Rx
# Generated: Thu Nov 21 21:11:18 2013
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

    def __init__(self, uhf_rx_gain=15, satellite_name="25544", control_port=5001, freq=437e6, predict_hostname="127.0.0.1", freq_error=0, predict_port=1210, iq_path=home_dir + "/data/iq/" + timestamp + ".iq"):
        gr.top_block.__init__(self, "Beacon Rx")

        ##################################################
        # Parameters
        ##################################################
        self.uhf_rx_gain = uhf_rx_gain
        self.satellite_name = satellite_name
        self.control_port = control_port
        self.freq = freq
        self.predict_hostname = predict_hostname
        self.freq_error = freq_error
        self.predict_port = predict_port
        self.iq_path = iq_path

        ##################################################
        # Variables
        ##################################################
        self.timestamp = timestamp =  str(time.gmtime().tm_year) + time.strftime("%m%d-%H%M",time.gmtime())
        self.samp_rate = samp_rate = 400e3
        self.home_dir = home_dir = "/home/nanosatisfi/"
        self.filename = filename = '/home/nanosatisfi/data/audio' + timestamp + '.wav'
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
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq,10e6), 0)
        self.uhd_usrp_source_0.set_gain(uhf_rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.satisfi_predict_query_0 = satisfi.predict_query(predict_ip=predict_hostname,predict_port=predict_port,sat_name=satellite_name,freq=freq,xml_port=control_port,xml_ip="127.0.0.1")
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=10,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/10)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "iq_path")
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(40000, analog.GR_COS_WAVE, -doppler_shift-freq_error, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0_0, "strobe", self.satisfi_predict_query_0, "trig")

# QT sink close method reimplementation

    def get_uhf_rx_gain(self):
        return self.uhf_rx_gain

    def set_uhf_rx_gain(self, uhf_rx_gain):
        self.uhf_rx_gain = uhf_rx_gain
        self.uhd_usrp_source_0.set_gain(self.uhf_rx_gain, 0)

    def get_satellite_name(self):
        return self.satellite_name

    def set_satellite_name(self, satellite_name):
        self.satellite_name = satellite_name
        self.satisfi_predict_query_0.set_name(self.satellite_name)

    def get_control_port(self):
        return self.control_port

    def set_control_port(self, control_port):
        self.control_port = control_port

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,10e6), 0)
        self.satisfi_predict_query_0.set_freq(self.freq)

    def get_predict_hostname(self):
        return self.predict_hostname

    def set_predict_hostname(self, predict_hostname):
        self.predict_hostname = predict_hostname

    def get_freq_error(self):
        return self.freq_error

    def set_freq_error(self, freq_error):
        self.freq_error = freq_error
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

    def get_predict_port(self):
        return self.predict_port

    def set_predict_port(self, predict_port):
        self.predict_port = predict_port

    def get_iq_path(self):
        return self.iq_path

    def set_iq_path(self, iq_path):
        self.iq_path = iq_path

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        self.set_filename('/home/nanosatisfi/data/audio' + self.timestamp + '.wav')

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/10)

    def get_home_dir(self):
        return self.home_dir

    def set_home_dir(self, home_dir):
        self.home_dir = home_dir

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--uhf-rx-gain", dest="uhf_rx_gain", type="eng_float", default=eng_notation.num_to_str(15),
        help="Set uhf_rx_gain [default=%default]")
    parser.add_option("", "--satellite-name", dest="satellite_name", type="string", default="25544",
        help="Set satellite_name [default=%default]")
    parser.add_option("", "--control-port", dest="control_port", type="intx", default=5001,
        help="Set control_port [default=%default]")
    parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(437e6),
        help="Set freq [default=%default]")
    parser.add_option("", "--predict-hostname", dest="predict_hostname", type="string", default="127.0.0.1",
        help="Set predict_hostname [default=%default]")
    parser.add_option("", "--freq-error", dest="freq_error", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set freq_error [default=%default]")
    parser.add_option("", "--predict-port", dest="predict_port", type="intx", default=1210,
        help="Set predict_port [default=%default]")
    parser.add_option("", "--iq-path", dest="iq_path", type="string", default=home_dir + "/data/iq/" + timestamp + ".iq",
        help="Set iq_path [default=%default]")
    (options, args) = parser.parse_args()
    tb = beacon_rx(uhf_rx_gain=options.uhf_rx_gain, satellite_name=options.satellite_name, control_port=options.control_port, freq=options.freq, predict_hostname=options.predict_hostname, freq_error=options.freq_error, predict_port=options.predict_port, iq_path=options.iq_path)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

