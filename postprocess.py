#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Postprocess
# Generated: Mon Oct 14 22:25:53 2013
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
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import satisfi
import wx

class postprocess(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Postprocess")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.wpm = wpm = 15
        self.width = width = 200
        self.wid2 = wid2 = 80
        self.volume = volume = 1
        self.tone_freq = tone_freq = 1000
        self.thresh = thresh = 0.004
        self.signal = signal = 0.12
        self.samp_rate = samp_rate = 40000
        self.reference = reference = 0.015
        self.noise = noise = 0.5
        self.lpf2 = lpf2 = 20
        self.freq_adjust = freq_adjust = 0
        self.detect_level = detect_level = 0.002
        self.decay = decay = 1e-6
        self.avg_len = avg_len = 1
        self.attack = attack = 0.6

        ##################################################
        # Blocks
        ##################################################
        self.nb0 = self.nb0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb0.AddPage(grc_wxgui.Panel(self.nb0), "Baseband")
        self.nb0.AddPage(grc_wxgui.Panel(self.nb0), "Morse Decoder")
        self.GridAdd(self.nb0, 0, 0, 1, 1)
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label='width',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._width_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	minimum=100,
        	maximum=2000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(1).Add(_width_sizer)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=100,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(0).Add(_volume_sizer)
        _tone_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone_freq_text_box = forms.text_box(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_tone_freq_sizer,
        	value=self.tone_freq,
        	callback=self.set_tone_freq,
        	label='tone_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone_freq_slider = forms.slider(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_tone_freq_sizer,
        	value=self.tone_freq,
        	callback=self.set_tone_freq,
        	minimum=0,
        	maximum=1000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(0).Add(_tone_freq_sizer)
        self._thresh_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	value=self.thresh,
        	callback=self.set_thresh,
        	label='thresh',
        	converter=forms.float_converter(),
        )
        self.nb0.GetPage(1).GridAdd(self._thresh_text_box, 1, 1, 1, 1)
        _reference_sizer = wx.BoxSizer(wx.VERTICAL)
        self._reference_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_reference_sizer,
        	value=self.reference,
        	callback=self.set_reference,
        	label="AGC3 Reference",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._reference_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_reference_sizer,
        	value=self.reference,
        	callback=self.set_reference,
        	minimum=0.00000001,
        	maximum=5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(1).GridAdd(_reference_sizer, 3, 0, 1, 1)
        self._lpf2_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	value=self.lpf2,
        	callback=self.set_lpf2,
        	label='lpf2',
        	converter=forms.float_converter(),
        )
        self.nb0.GetPage(1).GridAdd(self._lpf2_text_box, 3, 1, 1, 1)
        _freq_adjust_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_adjust_text_box = forms.text_box(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_freq_adjust_sizer,
        	value=self.freq_adjust,
        	callback=self.set_freq_adjust,
        	label='freq_adjust',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_adjust_slider = forms.slider(
        	parent=self.nb0.GetPage(0).GetWin(),
        	sizer=_freq_adjust_sizer,
        	value=self.freq_adjust,
        	callback=self.set_freq_adjust,
        	minimum=-10000,
        	maximum=10000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(0).Add(_freq_adjust_sizer)
        _decay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._decay_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_decay_sizer,
        	value=self.decay,
        	callback=self.set_decay,
        	label="AGC3 Decay",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._decay_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_decay_sizer,
        	value=self.decay,
        	callback=self.set_decay,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(1).GridAdd(_decay_sizer, 1, 0, 1, 1)
        _avg_len_sizer = wx.BoxSizer(wx.VERTICAL)
        self._avg_len_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_avg_len_sizer,
        	value=self.avg_len,
        	callback=self.set_avg_len,
        	label='avg_len',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._avg_len_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_avg_len_sizer,
        	value=self.avg_len,
        	callback=self.set_avg_len,
        	minimum=1,
        	maximum=500,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.nb0.GetPage(1).Add(_avg_len_sizer)
        _attack_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	label="AGC3 Attack",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._attack_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	minimum=0.00000001,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(1).GridAdd(_attack_sizer, 2, 0, 1, 1)
        self.wxgui_scopesink2_0_0_0_0_0_0_0 = scopesink2.scope_sink_f(
        	self.nb0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=9600,
        	v_scale=.001,
        	v_offset=.004,
        	t_scale=0.08,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=4,
        	trig_mode=wxgui.TRIG_MODE_STRIPCHART,
        	y_axis_label="Counts",
        )
        self.nb0.GetPage(1).GridAdd(self.wxgui_scopesink2_0_0_0_0_0_0_0.win, 0, 0, 1, 2)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb0.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=40000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.nb0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        _wid2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._wid2_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_wid2_sizer,
        	value=self.wid2,
        	callback=self.set_wid2,
        	label='wid2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._wid2_slider = forms.slider(
        	parent=self.nb0.GetPage(1).GetWin(),
        	sizer=_wid2_sizer,
        	value=self.wid2,
        	callback=self.set_wid2,
        	minimum=20,
        	maximum=200,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb0.GetPage(1).Add(_wid2_sizer)
        self._signal_text_box = forms.text_box(
        	parent=self.nb0.GetPage(1).GetWin(),
        	value=self.signal,
        	callback=self.set_signal,
        	label='signal',
        	converter=forms.float_converter(),
        )
        self.nb0.GetPage(1).GridAdd(self._signal_text_box, 2, 1, 1, 1)
        self.satisfi_morse_decode_0 = satisfi.morse_decode(wpm, 9600, thresh, avg_len, 1, 1, 1)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self._noise_text_box = forms.text_box(
        	parent=self.nb0.GetPage(0).GetWin(),
        	value=self.noise,
        	callback=self.set_noise,
        	label='noise',
        	converter=forms.float_converter(),
        )
        self.nb0.GetPage(0).Add(self._noise_text_box)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(10, firdes.low_pass(
        	1, 96000, lpf2, 50, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, width, 100, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0_0 = filter.hilbert_fc(512)
        self.decoder_tone_freq = analog.sig_source_c(96000, analog.GR_SIN_WAVE, 1000, 1, 0)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, "192.168.0.138", 8888, 32768, True)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((detect_level*3, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((detect_level, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((detect_level*2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(96000, analog.GR_COS_WAVE, tone_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -freq_adjust, 1, 0)
        self.analog_agc3_xx_0 = analog.agc3_cc(attack, decay, reference, 1.0)
        self.analog_agc3_xx_0.set_max_gain(100000)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.decoder_tone_freq, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.satisfi_morse_decode_0, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 1))
        self.connect((self.satisfi_morse_decode_0, 3), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.satisfi_morse_decode_0, 2), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.satisfi_morse_decode_0, 1), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.hilbert_fc_0_0, 0))
        self.connect((self.hilbert_fc_0_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.analog_agc3_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.satisfi_morse_decode_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_multiply_xx_0, 0))


# QT sink close method reimplementation

    def get_wpm(self):
        return self.wpm

    def set_wpm(self, wpm):
        self.wpm = wpm

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, 100, firdes.WIN_HAMMING, 6.76))
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)

    def get_wid2(self):
        return self.wid2

    def set_wid2(self, wid2):
        self.wid2 = wid2
        self._wid2_slider.set_value(self.wid2)
        self._wid2_text_box.set_value(self.wid2)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_tone_freq(self):
        return self.tone_freq

    def set_tone_freq(self, tone_freq):
        self.tone_freq = tone_freq
        self._tone_freq_slider.set_value(self.tone_freq)
        self._tone_freq_text_box.set_value(self.tone_freq)
        self.analog_sig_source_x_0_0.set_frequency(self.tone_freq)

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.satisfi_morse_decode_0.set_thresh(self.thresh)
        self._thresh_text_box.set_value(self.thresh)

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal
        self._signal_text_box.set_value(self.signal)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_reference(self):
        return self.reference

    def set_reference(self, reference):
        self.reference = reference
        self.analog_agc3_xx_0.set_reference(self.reference)
        self._reference_slider.set_value(self.reference)
        self._reference_text_box.set_value(self.reference)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self._noise_text_box.set_value(self.noise)

    def get_lpf2(self):
        return self.lpf2

    def set_lpf2(self, lpf2):
        self.lpf2 = lpf2
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, 96000, self.lpf2, 50, firdes.WIN_HAMMING, 6.76))
        self._lpf2_text_box.set_value(self.lpf2)

    def get_freq_adjust(self):
        return self.freq_adjust

    def set_freq_adjust(self, freq_adjust):
        self.freq_adjust = freq_adjust
        self._freq_adjust_slider.set_value(self.freq_adjust)
        self._freq_adjust_text_box.set_value(self.freq_adjust)
        self.analog_sig_source_x_0.set_frequency(-self.freq_adjust)

    def get_detect_level(self):
        return self.detect_level

    def set_detect_level(self, detect_level):
        self.detect_level = detect_level
        self.blocks_multiply_const_vxx_1_0.set_k((self.detect_level, ))
        self.blocks_multiply_const_vxx_1.set_k((self.detect_level*2, ))
        self.blocks_multiply_const_vxx_1_1.set_k((self.detect_level*3, ))

    def get_decay(self):
        return self.decay

    def set_decay(self, decay):
        self.decay = decay
        self._decay_slider.set_value(self.decay)
        self._decay_text_box.set_value(self.decay)
        self.analog_agc3_xx_0.set_decay_rate(self.decay)

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        self._avg_len_slider.set_value(self.avg_len)
        self._avg_len_text_box.set_value(self.avg_len)

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack
        self.analog_agc3_xx_0.set_attack_rate(self.attack)
        self._attack_slider.set_value(self.attack)
        self._attack_text_box.set_value(self.attack)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = postprocess()
    tb.Start(True)
    tb.Wait()

