#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Link Usrp Remote
# Generated: Thu Nov 21 07:50:37 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import pmt
import satisfi
import wx

class link_usrp_remote(grc_wxgui.top_block_gui):

    def __init__(self, uhf_freq_error=0, uhf_initial_datarate=9600, uhf_rx_gain=15, satellite_name="OSCAR-27", uhf_initial_freq=437e6, uhf_tx_gain=15, sband_rx_gain=15, tty_dev="/dev/pts/12", sband_initial_datarate=57600, sband_initial_freq=57600, sband_freq_error=0, uhf_usrp_address="", sband_usrp_address="", predict_hostname="127.0.0.1", predict_port=1210, control_port=5001, local_ip="192.168.0.179", rx_port=8818, remote_ip="192.168.0.187"):
        grc_wxgui.top_block_gui.__init__(self, title="Link Usrp Remote")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.uhf_freq_error = uhf_freq_error
        self.uhf_initial_datarate = uhf_initial_datarate
        self.uhf_rx_gain = uhf_rx_gain
        self.satellite_name = satellite_name
        self.uhf_initial_freq = uhf_initial_freq
        self.uhf_tx_gain = uhf_tx_gain
        self.sband_rx_gain = sband_rx_gain
        self.tty_dev = tty_dev
        self.sband_initial_datarate = sband_initial_datarate
        self.sband_initial_freq = sband_initial_freq
        self.sband_freq_error = sband_freq_error
        self.uhf_usrp_address = uhf_usrp_address
        self.sband_usrp_address = sband_usrp_address
        self.predict_hostname = predict_hostname
        self.predict_port = predict_port
        self.control_port = control_port
        self.local_ip = local_ip
        self.rx_port = rx_port
        self.remote_ip = remote_ip

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.freq = freq = uhf_initial_freq
        self.doppler_shift = doppler_shift = 0

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "fft")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "scope")
        self.Add(self.nb)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=48000,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=1024,
        	fft_rate=10,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.nb.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.satisfi_sync_to_pdu_0 = satisfi.sync_to_pdu()
        self.satisfi_serial_io_0 = satisfi.serial_io(tty_dev,0,57600,0,1,False)
        self.satisfi_predict_query_0 = satisfi.predict_query(predict_ip=predict_hostname,predict_port=predict_port,sat_name=satellite_name,freq=freq,xml_port=control_port,xml_ip="127.0.0.1")
        self.satisfi_pdu_link_0 = satisfi.pdu_link()
        self.satisfi_packet_framer_0 = satisfi.packet_framer(
            rs_enabled=True,
            conv_enabled=False,
            scrambler_enabled=True,
            preamble_length=2,
            trailer_length=2,
        )
        self.satisfi_mac_0 = satisfi.mac(self_tx_guard=.003,incoming_tx_guard=.03,packet_delay=0,first_preamble=30,next_preamble=30,data_rate=9600)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48000, 6e3, 500, firdes.WIN_HAMMING, 6.76))
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=5,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.digital_correlate_access_code_bb_0 = digital.correlate_access_code_bb("11000011101010100110011001010101", 3)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, local_ip, rx_port, 38724, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, remote_ip, 8888, 38724, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 48000)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "packet_len")
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((1000, ))
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("TEST"), 500)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(48000, analog.GR_COS_WAVE, 7.2e3, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.satisfi_sync_to_pdu_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.digital_correlate_access_code_bb_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_udp_sink_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.satisfi_sync_to_pdu_0, "out", self.satisfi_pdu_link_0, "pdu_in")
        self.msg_connect(self.satisfi_pdu_link_0, "binary_out", self.satisfi_serial_io_0, "in")
        self.msg_connect(self.satisfi_serial_io_0, "out", self.satisfi_pdu_link_0, "binary_in")
        self.msg_connect(self.satisfi_packet_framer_0, "out", self.satisfi_mac_0, "data_in")
        self.msg_connect(self.satisfi_mac_0, "data_out", self.blocks_pdu_to_tagged_stream_0, "pdus")
        self.msg_connect(self.satisfi_sync_to_pdu_0, "ctrl_out", self.satisfi_mac_0, "ctrl_in")
        self.msg_connect(self.blocks_message_strobe_0, "strobe", self.satisfi_mac_0, "beat_in")
        self.msg_connect(self.satisfi_pdu_link_0, "pdu_out", self.satisfi_packet_framer_0, "in")
        self.msg_connect(self.blocks_message_strobe_0_0, "strobe", self.satisfi_predict_query_0, "trig")

# QT sink close method reimplementation

    def get_uhf_freq_error(self):
        return self.uhf_freq_error

    def set_uhf_freq_error(self, uhf_freq_error):
        self.uhf_freq_error = uhf_freq_error

    def get_uhf_initial_datarate(self):
        return self.uhf_initial_datarate

    def set_uhf_initial_datarate(self, uhf_initial_datarate):
        self.uhf_initial_datarate = uhf_initial_datarate

    def get_uhf_rx_gain(self):
        return self.uhf_rx_gain

    def set_uhf_rx_gain(self, uhf_rx_gain):
        self.uhf_rx_gain = uhf_rx_gain

    def get_satellite_name(self):
        return self.satellite_name

    def set_satellite_name(self, satellite_name):
        self.satellite_name = satellite_name
        self.satisfi_predict_query_0.set_name(self.satellite_name)

    def get_uhf_initial_freq(self):
        return self.uhf_initial_freq

    def set_uhf_initial_freq(self, uhf_initial_freq):
        self.uhf_initial_freq = uhf_initial_freq
        self.set_freq(self.uhf_initial_freq)

    def get_uhf_tx_gain(self):
        return self.uhf_tx_gain

    def set_uhf_tx_gain(self, uhf_tx_gain):
        self.uhf_tx_gain = uhf_tx_gain

    def get_sband_rx_gain(self):
        return self.sband_rx_gain

    def set_sband_rx_gain(self, sband_rx_gain):
        self.sband_rx_gain = sband_rx_gain

    def get_tty_dev(self):
        return self.tty_dev

    def set_tty_dev(self, tty_dev):
        self.tty_dev = tty_dev

    def get_sband_initial_datarate(self):
        return self.sband_initial_datarate

    def set_sband_initial_datarate(self, sband_initial_datarate):
        self.sband_initial_datarate = sband_initial_datarate

    def get_sband_initial_freq(self):
        return self.sband_initial_freq

    def set_sband_initial_freq(self, sband_initial_freq):
        self.sband_initial_freq = sband_initial_freq

    def get_sband_freq_error(self):
        return self.sband_freq_error

    def set_sband_freq_error(self, sband_freq_error):
        self.sband_freq_error = sband_freq_error

    def get_uhf_usrp_address(self):
        return self.uhf_usrp_address

    def set_uhf_usrp_address(self, uhf_usrp_address):
        self.uhf_usrp_address = uhf_usrp_address

    def get_sband_usrp_address(self):
        return self.sband_usrp_address

    def set_sband_usrp_address(self, sband_usrp_address):
        self.sband_usrp_address = sband_usrp_address

    def get_predict_hostname(self):
        return self.predict_hostname

    def set_predict_hostname(self, predict_hostname):
        self.predict_hostname = predict_hostname

    def get_predict_port(self):
        return self.predict_port

    def set_predict_port(self, predict_port):
        self.predict_port = predict_port

    def get_control_port(self):
        return self.control_port

    def set_control_port(self, control_port):
        self.control_port = control_port

    def get_local_ip(self):
        return self.local_ip

    def set_local_ip(self, local_ip):
        self.local_ip = local_ip

    def get_rx_port(self):
        return self.rx_port

    def set_rx_port(self, rx_port):
        self.rx_port = rx_port

    def get_remote_ip(self):
        return self.remote_ip

    def set_remote_ip(self, remote_ip):
        self.remote_ip = remote_ip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.satisfi_predict_query_0.set_freq(self.freq)

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--uhf-freq-error", dest="uhf_freq_error", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set uhf_freq_error [default=%default]")
    parser.add_option("", "--uhf-initial-datarate", dest="uhf_initial_datarate", type="eng_float", default=eng_notation.num_to_str(9600),
        help="Set uhf_initial_datarate [default=%default]")
    parser.add_option("", "--uhf-rx-gain", dest="uhf_rx_gain", type="eng_float", default=eng_notation.num_to_str(15),
        help="Set uhf_rx_gain [default=%default]")
    parser.add_option("", "--satellite-name", dest="satellite_name", type="string", default="OSCAR-27",
        help="Set satellite_name [default=%default]")
    parser.add_option("", "--uhf-initial-freq", dest="uhf_initial_freq", type="eng_float", default=eng_notation.num_to_str(437e6),
        help="Set uhf_initial_freq [default=%default]")
    parser.add_option("", "--uhf-tx-gain", dest="uhf_tx_gain", type="intx", default=15,
        help="Set uhf_tx_gain [default=%default]")
    parser.add_option("", "--sband-rx-gain", dest="sband_rx_gain", type="intx", default=15,
        help="Set sband_rx_gain [default=%default]")
    parser.add_option("", "--tty-dev", dest="tty_dev", type="string", default="/dev/pts/12",
        help="Set tty_dev [default=%default]")
    parser.add_option("", "--sband-initial-datarate", dest="sband_initial_datarate", type="eng_float", default=eng_notation.num_to_str(57600),
        help="Set sband_initial_datarate [default=%default]")
    parser.add_option("", "--sband-initial-freq", dest="sband_initial_freq", type="eng_float", default=eng_notation.num_to_str(57600),
        help="Set sband_initial_freq [default=%default]")
    parser.add_option("", "--sband-freq-error", dest="sband_freq_error", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set sband_freq_error [default=%default]")
    parser.add_option("", "--uhf-usrp-address", dest="uhf_usrp_address", type="string", default="",
        help="Set uhf_usrp_address [default=%default]")
    parser.add_option("", "--sband-usrp-address", dest="sband_usrp_address", type="string", default="",
        help="Set sband_usrp_address [default=%default]")
    parser.add_option("", "--predict-hostname", dest="predict_hostname", type="string", default="127.0.0.1",
        help="Set predict_hostname [default=%default]")
    parser.add_option("", "--predict-port", dest="predict_port", type="intx", default=1210,
        help="Set predict_port [default=%default]")
    parser.add_option("", "--control-port", dest="control_port", type="intx", default=5001,
        help="Set control_port [default=%default]")
    parser.add_option("", "--local-ip", dest="local_ip", type="string", default="192.168.0.179",
        help="Set local_ip [default=%default]")
    parser.add_option("", "--rx-port", dest="rx_port", type="intx", default=8818,
        help="Set rx_port [default=%default]")
    parser.add_option("", "--remote-ip", dest="remote_ip", type="string", default="192.168.0.187",
        help="Set remote_ip [default=%default]")
    (options, args) = parser.parse_args()
    tb = link_usrp_remote(uhf_freq_error=options.uhf_freq_error, uhf_initial_datarate=options.uhf_initial_datarate, uhf_rx_gain=options.uhf_rx_gain, satellite_name=options.satellite_name, uhf_initial_freq=options.uhf_initial_freq, uhf_tx_gain=options.uhf_tx_gain, sband_rx_gain=options.sband_rx_gain, tty_dev=options.tty_dev, sband_initial_datarate=options.sband_initial_datarate, sband_initial_freq=options.sband_initial_freq, sband_freq_error=options.sband_freq_error, uhf_usrp_address=options.uhf_usrp_address, sband_usrp_address=options.sband_usrp_address, predict_hostname=options.predict_hostname, predict_port=options.predict_port, control_port=options.control_port, local_ip=options.local_ip, rx_port=options.rx_port, remote_ip=options.remote_ip)
    tb.Start(True)
    tb.Wait()

