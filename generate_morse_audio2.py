#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Generate Morse Audio2
# Generated: Mon Oct 14 13:12:11 2013
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

class generate_morse_audio2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Generate Morse Audio2")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.wpm = wpm = 50
        self.width2 = width2 = 50
        self.width = width = 200
        self.thresh = thresh = 0.002
        self.signal = signal = 0.15
        self.samp_rate = samp_rate = 96000
        self.reference = reference = 0.002
        self.noise = noise = 0.5
        self.letter_detect_true_level = letter_detect_true_level = 0.004
        self.freq_filter = freq_filter = 0
        self.freq = freq = 1000
        self.decay = decay = 0.01
        self.char_detect_true_level = char_detect_true_level = 0.002
        self.avg_len = avg_len = 1
        self.attack = attack = 0.1

        ##################################################
        # Blocks
        ##################################################
        self.nb1 = self.nb1 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb1.AddPage(grc_wxgui.Panel(self.nb1), "signal properties")
        self.nb1.AddPage(grc_wxgui.Panel(self.nb1), "morse decoder")
        self.Add(self.nb1)
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label="Signal Filter Width",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._width_slider = forms.slider(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	minimum=10,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(0).Add(_width_sizer)
        _signal_sizer = wx.BoxSizer(wx.VERTICAL)
        self._signal_text_box = forms.text_box(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	label="Signal Power",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._signal_slider = forms.slider(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(0).Add(_signal_sizer)
        _noise_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_text_box = forms.text_box(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	label="Noise Power",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_slider = forms.slider(
        	parent=self.nb1.GetPage(0).GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(0).Add(_noise_sizer)
        self.nb = self.nb = wx.Notebook(self.nb1.GetPage(0).GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "signal")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "downshift")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "filter+upshift")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "quadrature")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "mag2")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "fft")
        self.nb1.GetPage(0).Add(self.nb)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_scopesink2_0_0_0_0_0_0_0 = scopesink2.scope_sink_f(
        	self.nb1.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/10,
        	v_scale=.001,
        	v_offset=.004,
        	t_scale=0.08,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=4,
        	trig_mode=wxgui.TRIG_MODE_STRIPCHART,
        	y_axis_label="Counts",
        )
        self.nb1.GetPage(1).GridAdd(self.wxgui_scopesink2_0_0_0_0_0_0_0.win, 0, 0, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.nb.GetPage(5).GetWin(),
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
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.nb.GetPage(5).Add(self.wxgui_fftsink2_0.win)
        self.satisfi_morse_key_0 = satisfi.morse_key(wpm, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", True, samp_rate)
        self.satisfi_morse_decode_0 = satisfi.morse_decode(wpm, samp_rate/10, thresh, 1, 0.003, 0.004, 0.001)
        _reference_sizer = wx.BoxSizer(wx.VERTICAL)
        self._reference_text_box = forms.text_box(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_reference_sizer,
        	value=self.reference,
        	callback=self.set_reference,
        	label="Reference Value",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._reference_slider = forms.slider(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_reference_sizer,
        	value=self.reference,
        	callback=self.set_reference,
        	minimum=0,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(1).Add(_reference_sizer)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(10, firdes.low_pass(
        	1, samp_rate, width2, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, width, 100, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(512)
        _freq_filter_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_filter_text_box = forms.text_box(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_freq_filter_sizer,
        	value=self.freq_filter,
        	callback=self.set_freq_filter,
        	label='freq_filter',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_filter_slider = forms.slider(
        	parent=self.nb.GetPage(0).GetWin(),
        	sizer=_freq_filter_sizer,
        	value=self.freq_filter,
        	callback=self.set_freq_filter,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(0).Add(_freq_filter_sizer)
        _decay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._decay_text_box = forms.text_box(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_decay_sizer,
        	value=self.decay,
        	callback=self.set_decay,
        	label="Decay Rate",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._decay_slider = forms.slider(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_decay_sizer,
        	value=self.decay,
        	callback=self.set_decay,
        	minimum=0.000001,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(1).Add(_decay_sizer)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0, ))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        _avg_len_sizer = wx.BoxSizer(wx.VERTICAL)
        self._avg_len_text_box = forms.text_box(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_avg_len_sizer,
        	value=self.avg_len,
        	callback=self.set_avg_len,
        	label='avg_len',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._avg_len_slider = forms.slider(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_avg_len_sizer,
        	value=self.avg_len,
        	callback=self.set_avg_len,
        	minimum=1,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.nb1.GetPage(1).Add(_avg_len_sizer)
        self.audio_sink_1 = audio.sink(samp_rate, "", True)
        _attack_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_text_box = forms.text_box(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	label="Attack Rate",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._attack_slider = forms.slider(
        	parent=self.nb1.GetPage(1).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	minimum=0.000001,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb1.GetPage(1).Add(_attack_sizer)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, -freq, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq, signal, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)
        self.analog_agc2_xx_0 = analog.agc2_ff(1e-1, 1e-2, 0.002, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.satisfi_morse_key_0, 0))
        self.connect((self.satisfi_morse_decode_0, 2), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 2))
        self.connect((self.satisfi_morse_decode_0, 1), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 1))
        self.connect((self.satisfi_morse_decode_0, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.satisfi_morse_decode_0, 0))
        self.connect((self.satisfi_morse_key_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.satisfi_morse_decode_0, 3), (self.blocks_null_sink_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.wxgui_scopesink2_0_0_0_0_0_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0_0, 0))


# QT sink close method reimplementation

    def get_wpm(self):
        return self.wpm

    def set_wpm(self, wpm):
        self.wpm = wpm
        self.satisfi_morse_key_0.set_wpm(self.wpm)

    def get_width2(self):
        return self.width2

    def set_width2(self, width2):
        self.width2 = width2
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width2, 100, firdes.WIN_HAMMING, 6.76))

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, 100, firdes.WIN_HAMMING, 6.76))

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.satisfi_morse_decode_0.set_thresh(self.thresh)

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal
        self.analog_sig_source_x_0.set_amplitude(self.signal)
        self._signal_slider.set_value(self.signal)
        self._signal_text_box.set_value(self.signal)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.wxgui_scopesink2_0_0_0_0_0_0_0.set_sample_rate(self.samp_rate/10)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width2, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)

    def get_reference(self):
        return self.reference

    def set_reference(self, reference):
        self.reference = reference
        self._reference_slider.set_value(self.reference)
        self._reference_text_box.set_value(self.reference)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)
        self._noise_slider.set_value(self.noise)
        self._noise_text_box.set_value(self.noise)

    def get_letter_detect_true_level(self):
        return self.letter_detect_true_level

    def set_letter_detect_true_level(self, letter_detect_true_level):
        self.letter_detect_true_level = letter_detect_true_level

    def get_freq_filter(self):
        return self.freq_filter

    def set_freq_filter(self, freq_filter):
        self.freq_filter = freq_filter
        self._freq_filter_slider.set_value(self.freq_filter)
        self._freq_filter_text_box.set_value(self.freq_filter)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.analog_sig_source_x_0_0.set_frequency(self.freq)
        self.analog_sig_source_x_0_0_0.set_frequency(-self.freq)

    def get_decay(self):
        return self.decay

    def set_decay(self, decay):
        self.decay = decay
        self._decay_slider.set_value(self.decay)
        self._decay_text_box.set_value(self.decay)

    def get_char_detect_true_level(self):
        return self.char_detect_true_level

    def set_char_detect_true_level(self, char_detect_true_level):
        self.char_detect_true_level = char_detect_true_level

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
        self._attack_slider.set_value(self.attack)
        self._attack_text_box.set_value(self.attack)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = generate_morse_audio2()
    tb.Start(True)
    tb.Wait()

