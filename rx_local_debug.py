#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Rx Local Debug
# Generated: Wed Mar 12 14:00:11 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class rx_local_debug(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Rx Local Debug")

        ##################################################
        # Variables
        ##################################################
        self.usrp_gain = usrp_gain = 5
        self.tracking = tracking = 0
        self.samp_rate = samp_rate = 1e6
        self.offset = offset = 0
        self.freq = freq = 401.829e6
        self.doppler_shift = doppler_shift = 0
        self.doppler_enable = doppler_enable = False
        self.adjust = adjust = 0
        self.LO_offset = LO_offset = 10e6

        ##################################################
        # Blocks
        ##################################################
        self._usrp_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.usrp_gain,
        	callback=self.set_usrp_gain,
        	label="USRP Rx Gain (dB)",
        	converter=forms.float_converter(),
        )
        self.Add(self._usrp_gain_text_box)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.offset,
        	callback=self.set_offset,
        	label="USRP Freq Error Offset (Hz)",
        	converter=forms.float_converter(),
        )
        self.Add(self._offset_text_box)
        self.nb0 = self.nb0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb0.AddPage(grc_wxgui.Panel(self.nb0), "FFT")
        self.nb0.AddPage(grc_wxgui.Panel(self.nb0), "Waterfall")
        self.Add(self.nb0)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Center Frequency (Hz)",
        	converter=forms.float_converter(),
        )
        self.Add(self._freq_text_box)
        self._doppler_enable_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.doppler_enable,
        	callback=self.set_doppler_enable,
        	label="Doppler Correction Enable",
        	true=1,
        	false=0,
        )
        self.Add(self._doppler_enable_check_box)
        _adjust_sizer = wx.BoxSizer(wx.VERTICAL)
        self._adjust_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_adjust_sizer,
        	value=self.adjust,
        	callback=self.set_adjust,
        	label='adjust',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._adjust_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_adjust_sizer,
        	value=self.adjust,
        	callback=self.set_adjust,
        	minimum=-10e3,
        	maximum=10e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_adjust_sizer)
        self._LO_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.LO_offset,
        	callback=self.set_LO_offset,
        	label="USRP LO Offset (Hz)",
        	converter=forms.float_converter(),
        )
        self.Add(self._LO_offset_text_box)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb0.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/1,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Wide FFt",
        	peak_hold=False,
        )
        self.nb0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="addr=192.168.10.3",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq+offset,LO_offset), 0)
        self.uhd_usrp_source_0.set_gain(usrp_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self._tracking_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.tracking,
        	callback=self.set_tracking,
        	label='tracking',
        	converter=forms.float_converter(),
        )
        self.Add(self._tracking_static_text)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/jspark/sample_interference.iq", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/1, analog.GR_COS_WAVE, -adjust-(doppler_shift*doppler_enable), 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0, 0))


# QT sink close method reimplementation

    def get_usrp_gain(self):
        return self.usrp_gain

    def set_usrp_gain(self, usrp_gain):
        self.usrp_gain = usrp_gain
        self._usrp_gain_text_box.set_value(self.usrp_gain)
        self.uhd_usrp_source_0.set_gain(self.usrp_gain, 0)

    def get_tracking(self):
        return self.tracking

    def set_tracking(self, tracking):
        self.tracking = tracking
        self._tracking_static_text.set_value(self.tracking)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/1)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/1)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_text_box.set_value(self.offset)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.offset,self.LO_offset), 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_text_box.set_value(self.freq)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.offset,self.LO_offset), 0)

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.analog_sig_source_x_0.set_frequency(-self.adjust-(self.doppler_shift*self.doppler_enable))

    def get_doppler_enable(self):
        return self.doppler_enable

    def set_doppler_enable(self, doppler_enable):
        self.doppler_enable = doppler_enable
        self._doppler_enable_check_box.set_value(self.doppler_enable)
        self.analog_sig_source_x_0.set_frequency(-self.adjust-(self.doppler_shift*self.doppler_enable))

    def get_adjust(self):
        return self.adjust

    def set_adjust(self, adjust):
        self.adjust = adjust
        self._adjust_slider.set_value(self.adjust)
        self._adjust_text_box.set_value(self.adjust)
        self.analog_sig_source_x_0.set_frequency(-self.adjust-(self.doppler_shift*self.doppler_enable))

    def get_LO_offset(self):
        return self.LO_offset

    def set_LO_offset(self, LO_offset):
        self.LO_offset = LO_offset
        self._LO_offset_text_box.set_value(self.LO_offset)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.offset,self.LO_offset), 0)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = rx_local_debug()
    tb.Start(True)
    tb.Wait()

