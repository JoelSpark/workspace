#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: SSB 
# Generated: Sun Oct 13 15:11:59 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
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

class SSB_Rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="SSB ")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.notch_freq = notch_freq = 0
        self.freq = freq = 437.000e6
        self.volume = volume = 1
        self.usrp_gain = usrp_gain = 10
        self.tone_freq = tone_freq = 1e3
        self.samp_rate = samp_rate = 400000
        self.notch_width = notch_width = 500
        self.lo_offset = lo_offset = 10e3
        self.error_tune = error_tune = -9.3e3
        self.decimation = decimation = 10
        self.currect_freq_center = currect_freq_center = freq+notch_freq

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Spectrum")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "USRP Settings")
        self.GridAdd(self.nb, 0, 0, 1, 1)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=10,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_volume_sizer, 5, 0, 1, 1)
        self._usrp_gain_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.usrp_gain,
        	callback=self.set_usrp_gain,
        	label="USRP Gain",
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).Add(self._usrp_gain_text_box)
        _tone_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone_freq_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_tone_freq_sizer,
        	value=self.tone_freq,
        	callback=self.set_tone_freq,
        	label="Tone Frequency (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone_freq_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_tone_freq_sizer,
        	value=self.tone_freq,
        	callback=self.set_tone_freq,
        	minimum=0,
        	maximum=9e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_tone_freq_sizer, 6, 0, 1, 1)
        _notch_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._notch_width_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_notch_width_sizer,
        	value=self.notch_width,
        	callback=self.set_notch_width,
        	label="Notch Width (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._notch_width_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_notch_width_sizer,
        	value=self.notch_width,
        	callback=self.set_notch_width,
        	minimum=100,
        	maximum=1e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_notch_width_sizer, 4, 0, 1, 1)
        _notch_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._notch_freq_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_notch_freq_sizer,
        	value=self.notch_freq,
        	callback=self.set_notch_freq,
        	label="Notch Offset (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._notch_freq_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_notch_freq_sizer,
        	value=self.notch_freq,
        	callback=self.set_notch_freq,
        	minimum=0,
        	maximum=10e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).GridAdd(_notch_freq_sizer, 3, 0, 1, 1)
        self.nb2 = self.nb2 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb2.AddPage(grc_wxgui.Panel(self.nb2), "Filtered")
        self.nb2.AddPage(grc_wxgui.Panel(self.nb2), "Raw Spectrum")
        self.GridAdd(self.nb2, 0, 1, 1, 1)
        self._lo_offset_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	value=self.lo_offset,
        	callback=self.set_lo_offset,
        	label="LO Offset (Hz)",
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(1).Add(self._lo_offset_text_box)
        self._freq_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Center Frequency (Hz)",
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._freq_text_box, 2, 0, 1, 1)
        _error_tune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._error_tune_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_error_tune_sizer,
        	value=self.error_tune,
        	callback=self.set_error_tune,
        	label="USRP Error Tune (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._error_tune_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_error_tune_sizer,
        	value=self.error_tune,
        	callback=self.set_error_tune,
        	minimum=-15e3,
        	maximum=15e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).GridAdd(_error_tune_sizer, 4, 0, 1, 1)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.nb2.GetPage(1).GetWin(),
        	baseband_freq=freq+error_tune,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=40000,
        	fft_size=2048,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	win=window.hamming,
        )
        self.nb2.GetPage(1).GridAdd(self.wxgui_fftsink2_0_0.win, 1, 1, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb2.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=40000,
        	fft_size=2048,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	win=window.hamming,
        )
        self.nb2.GetPage(0).GridAdd(self.wxgui_fftsink2_0.win, 1, 1, 1, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq+error_tune,lo_offset), 0)
        self.uhd_usrp_source_0.set_gain(usrp_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimation,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decimation, notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))
        self._currect_freq_center_static_text = forms.static_text(
        	parent=self.nb.GetPage(0).GetWin(),
        	value=self.currect_freq_center,
        	callback=self.set_currect_freq_center,
        	label="Center Freq (Actual)",
        	converter=forms.float_converter(),
        )
        self.nb.GetPage(0).GridAdd(self._currect_freq_center_static_text, 1, 0, 1, 1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.audio_sink_0 = audio.sink(96000, "", True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate/decimation, analog.GR_COS_WAVE, tone_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/decimation, analog.GR_COS_WAVE, notch_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.wxgui_fftsink2_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_notch_freq(self):
        return self.notch_freq

    def set_notch_freq(self, notch_freq):
        self.notch_freq = notch_freq
        self.analog_sig_source_x_0.set_frequency(self.notch_freq)
        self._notch_freq_slider.set_value(self.notch_freq)
        self._notch_freq_text_box.set_value(self.notch_freq)
        self.set_currect_freq_center(self.freq+self.notch_freq)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.error_tune,self.lo_offset), 0)
        self.set_currect_freq_center(self.freq+self.notch_freq)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.freq+self.error_tune)
        self._freq_text_box.set_value(self.freq)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_usrp_gain(self):
        return self.usrp_gain

    def set_usrp_gain(self, usrp_gain):
        self.usrp_gain = usrp_gain
        self._usrp_gain_text_box.set_value(self.usrp_gain)
        self.uhd_usrp_source_0.set_gain(self.usrp_gain, 0)

    def get_tone_freq(self):
        return self.tone_freq

    def set_tone_freq(self, tone_freq):
        self.tone_freq = tone_freq
        self._tone_freq_slider.set_value(self.tone_freq)
        self._tone_freq_text_box.set_value(self.tone_freq)
        self.analog_sig_source_x_0_0.set_frequency(self.tone_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decimation)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decimation)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimation, self.notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))

    def get_notch_width(self):
        return self.notch_width

    def set_notch_width(self, notch_width):
        self.notch_width = notch_width
        self._notch_width_slider.set_value(self.notch_width)
        self._notch_width_text_box.set_value(self.notch_width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimation, self.notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.error_tune,self.lo_offset), 0)
        self._lo_offset_text_box.set_value(self.lo_offset)

    def get_error_tune(self):
        return self.error_tune

    def set_error_tune(self, error_tune):
        self.error_tune = error_tune
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq+self.error_tune,self.lo_offset), 0)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.freq+self.error_tune)
        self._error_tune_slider.set_value(self.error_tune)
        self._error_tune_text_box.set_value(self.error_tune)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decimation)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decimation)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimation, self.notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))

    def get_currect_freq_center(self):
        return self.currect_freq_center

    def set_currect_freq_center(self, currect_freq_center):
        self.currect_freq_center = currect_freq_center
        self._currect_freq_center_static_text.set_value(self.currect_freq_center)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = SSB_Rx()
    tb.Start(True)
    tb.Wait()

