#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Stream Rx
# Generated: Wed Dec  4 01:51:12 2013
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
import time

class stream_rx(gr.top_block):

    def __init__(self, freq=437e6, freq_error=0, predict_port=1210, predict_hostname="127.0.0.1", control_port=5001, satellite_name="39413", fwd_to_ip="192.168.0.183", uhf_rx_gain=5):
        gr.top_block.__init__(self, "Stream Rx")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.freq_error = freq_error
        self.predict_port = predict_port
        self.predict_hostname = predict_hostname
        self.control_port = control_port
        self.satellite_name = satellite_name
        self.fwd_to_ip = fwd_to_ip
        self.uhf_rx_gain = uhf_rx_gain

        ##################################################
        # Variables
        ##################################################
        self.timestamp = timestamp =  str(time.gmtime().tm_year) + time.strftime("%m%d-%H%M",time.gmtime())
        self.wav_path = wav_path = '/home/nanosatisfi/data/audio' + timestamp + '.wav'
        self.samp_rate = samp_rate = 250e3
        self.iq_path = iq_path = '/home/nanosatisfi/data/iq/' + timestamp + '.iq'
        self.interpolation = interpolation = 96
        self.doppler_shift = doppler_shift = 0
        self.decimation = decimation = 250

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
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq,10e6), 0)
        self.uhd_usrp_source_0.set_gain(uhf_rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interpolation,
                decimation=decimation,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, fwd_to_ip, 8888, 32768, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate/decimation*interpolation, analog.GR_COS_WAVE, -doppler_shift-freq_error, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_udp_sink_0, 0))


# QT sink close method reimplementation

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,10e6), 0)

    def get_freq_error(self):
        return self.freq_error

    def set_freq_error(self, freq_error):
        self.freq_error = freq_error
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

    def get_predict_port(self):
        return self.predict_port

    def set_predict_port(self, predict_port):
        self.predict_port = predict_port

    def get_predict_hostname(self):
        return self.predict_hostname

    def set_predict_hostname(self, predict_hostname):
        self.predict_hostname = predict_hostname

    def get_control_port(self):
        return self.control_port

    def set_control_port(self, control_port):
        self.control_port = control_port

    def get_satellite_name(self):
        return self.satellite_name

    def set_satellite_name(self, satellite_name):
        self.satellite_name = satellite_name

    def get_fwd_to_ip(self):
        return self.fwd_to_ip

    def set_fwd_to_ip(self, fwd_to_ip):
        self.fwd_to_ip = fwd_to_ip

    def get_uhf_rx_gain(self):
        return self.uhf_rx_gain

    def set_uhf_rx_gain(self, uhf_rx_gain):
        self.uhf_rx_gain = uhf_rx_gain
        self.uhd_usrp_source_0.set_gain(self.uhf_rx_gain, 0)

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        self.set_iq_path('/home/nanosatisfi/data/iq/' + self.timestamp + '.iq')
        self.set_wav_path('/home/nanosatisfi/data/audio' + self.timestamp + '.wav')

    def get_wav_path(self):
        return self.wav_path

    def set_wav_path(self, wav_path):
        self.wav_path = wav_path

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decimation*self.interpolation)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_iq_path(self):
        return self.iq_path

    def set_iq_path(self, iq_path):
        self.iq_path = iq_path

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decimation*self.interpolation)

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.analog_sig_source_x_0_0.set_frequency(-self.doppler_shift-self.freq_error)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decimation*self.interpolation)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(437e6),
        help="Set freq [default=%default]")
    parser.add_option("", "--freq-error", dest="freq_error", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set freq_error [default=%default]")
    parser.add_option("", "--predict-port", dest="predict_port", type="intx", default=1210,
        help="Set predict_port [default=%default]")
    parser.add_option("", "--predict-hostname", dest="predict_hostname", type="string", default="127.0.0.1",
        help="Set predict_hostname [default=%default]")
    parser.add_option("", "--control-port", dest="control_port", type="intx", default=5001,
        help="Set control_port [default=%default]")
    parser.add_option("", "--satellite-name", dest="satellite_name", type="string", default="39413",
        help="Set satellite_name [default=%default]")
    parser.add_option("", "--fwd-to-ip", dest="fwd_to_ip", type="string", default="192.168.0.183",
        help="Set fwd_to_ip [default=%default]")
    parser.add_option("", "--uhf-rx-gain", dest="uhf_rx_gain", type="eng_float", default=eng_notation.num_to_str(5),
        help="Set uhf_rx_gain [default=%default]")
    (options, args) = parser.parse_args()
    tb = stream_rx(freq=options.freq, freq_error=options.freq_error, predict_port=options.predict_port, predict_hostname=options.predict_hostname, control_port=options.control_port, satellite_name=options.satellite_name, fwd_to_ip=options.fwd_to_ip, uhf_rx_gain=options.uhf_rx_gain)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

