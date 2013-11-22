#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Iq To Wav
# Generated: Thu Nov 21 21:11:12 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
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

class iq_to_wav(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Iq To Wav")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.width = width = 500
        self.trans = trans = 200
        self.samp_rate = samp_rate = 40000
        self.offset = offset = 0

        ##################################################
        # Blocks
        ##################################################
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label='width',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	minimum=100,
        	maximum=9e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_width_sizer)
        _trans_sizer = wx.BoxSizer(wx.VERTICAL)
        self._trans_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	label='trans',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._trans_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	minimum=20,
        	maximum=1e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_trans_sizer)
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label='offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=0,
        	maximum=16e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_offset_sizer)
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "raw")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "filtered")
        self.Add(self.nb)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.nb.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, width, trans, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/jspark/1.wav", 1, 48000, 8)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/jspark/IQ", False)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -offset, 1, 0)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=40000,
        	quad_rate=40000,
        	tau=75e-6,
        	max_dev=5e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_wavfile_sink_0, 0))


# QT sink close method reimplementation

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)

    def get_trans(self):
        return self.trans

    def set_trans(self, trans):
        self.trans = trans
        self._trans_slider.set_value(self.trans)
        self._trans_text_box.set_value(self.trans)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)
        self.analog_sig_source_x_0.set_frequency(-self.offset)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = iq_to_wav()
    tb.Start(True)
    tb.Wait()

