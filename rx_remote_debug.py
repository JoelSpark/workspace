#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Rx Remote Debug
# Generated: Thu Nov 21 21:14:31 2013
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class rx_remote_debug(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Rx Remote Debug")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.usrp_gain = usrp_gain = 0
        self.samp_rate = samp_rate = 40000
        self.offset = offset = 0
        self.freq = freq = 437.25e6
        self.LO_offset = LO_offset = 10e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=2048,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Wide FFt",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
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
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Center Frequency (Hz)",
        	converter=forms.float_converter(),
        )
        self.Add(self._freq_text_box)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, "192.168.0.128", 8888, 32768, True)
        self._LO_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.LO_offset,
        	callback=self.set_LO_offset,
        	label="USRP LO Offset (Hz)",
        	converter=forms.float_converter(),
        )
        self.Add(self._LO_offset_text_box)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_udp_source_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_usrp_gain(self):
        return self.usrp_gain

    def set_usrp_gain(self, usrp_gain):
        self.usrp_gain = usrp_gain
        self._usrp_gain_text_box.set_value(self.usrp_gain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_text_box.set_value(self.offset)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_text_box.set_value(self.freq)

    def get_LO_offset(self):
        return self.LO_offset

    def set_LO_offset(self, LO_offset):
        self.LO_offset = LO_offset
        self._LO_offset_text_box.set_value(self.LO_offset)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = rx_remote_debug()
    tb.Start(True)
    tb.Wait()

