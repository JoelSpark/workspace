#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Auto Ground Station CW Recorder
# Author: Joel Spark
# Generated: Sun Oct 13 19:43:23 2013
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
import SimpleXMLRPCServer
import pmt
import satisfi
import threading
import time
import wx

class auto_gs_cw(grc_wxgui.top_block_gui):

    def __init__(self, freq=437365000, sat="24278"):
        grc_wxgui.top_block_gui.__init__(self, title="Auto Ground Station CW Recorder")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.sat = sat

        ##################################################
        # Variables
        ##################################################
        self.timestamp = timestamp =  str(time.gmtime().tm_year) + time.strftime("%m%d_%H%M",time.gmtime())
        self.doppler_shift = doppler_shift = 0
        self.volume = volume = 10
        self.variable_static_text_0_0_0_0 = variable_static_text_0_0_0_0 = freq/1000000
        self.variable_static_text_0_0_0 = variable_static_text_0_0_0 = (freq+doppler_shift)/1000000
        self.variable_static_text_0_0 = variable_static_text_0_0 = sat
        self.variable_static_text_0 = variable_static_text_0 = doppler_shift
        self.tone_freq = tone_freq = 1e3
        self.samp_rate = samp_rate = 40000
        self.notch_width = notch_width = 1e3
        self.notch_freq = notch_freq = 0
        self.audio_filename = audio_filename = ('/home/jspark/data/audio/' + timestamp + '_' + sat + '.wav').replace(" ","_")

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
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
        self.Add(_volume_sizer)
        _tone_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tone_freq_sizer,
        	value=self.tone_freq,
        	callback=self.set_tone_freq,
        	label="Tone Frequency (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone_freq_slider = forms.slider(
        	parent=self.GetWin(),
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
        self.Add(_tone_freq_sizer)
        _notch_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._notch_width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_notch_width_sizer,
        	value=self.notch_width,
        	callback=self.set_notch_width,
        	label="Notch Width (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._notch_width_slider = forms.slider(
        	parent=self.GetWin(),
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
        self.Add(_notch_width_sizer)
        _notch_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._notch_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_notch_freq_sizer,
        	value=self.notch_freq,
        	callback=self.set_notch_freq,
        	label="Notch Offset (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._notch_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_notch_freq_sizer,
        	value=self.notch_freq,
        	callback=self.set_notch_freq,
        	minimum=-10e3,
        	maximum=10e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_notch_freq_sizer)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8808), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        threading.Thread(target=self.xmlrpc_server_0.serve_forever).start()
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=-40,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=2048,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.28,
        	title="FFT Plot",
        	peak_hold=False,
        	win=window.hamming,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        self._variable_static_text_0_0_0_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0_0_0_0,
        	callback=self.set_variable_static_text_0_0_0_0,
        	label="Center Frequency",
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_0_0_0_static_text)
        self._variable_static_text_0_0_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0_0_0,
        	callback=self.set_variable_static_text_0_0_0,
        	label="Current Frequency",
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_0_0_static_text)
        self._variable_static_text_0_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0_0,
        	callback=self.set_variable_static_text_0_0,
        	label="Sattelite ID",
        	converter=forms.str_converter(),
        )
        self.Add(self._variable_static_text_0_0_static_text)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label="Doppler Shift",
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_static_text_0_static_text)
        self.satisfi_predict_query_0 = satisfi.predict_query(predict_ip="127.0.0.1",predict_port=1210,sat_name=sat,freq=freq,xml_port=8808,xml_ip="127.0.0.1")
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=6,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/jspark/data/audio/fo29.wav", 1, 48000, 16)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, "192.168.0.138", 8888, 32768, True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 100)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/jspark/data/iq/fo29")
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -notch_freq, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, tone_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -doppler_shift, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.wxgui_fftsink2_0_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0, "strobe", self.satisfi_predict_query_0, "trig")

# QT sink close method reimplementation

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_variable_static_text_0_0_0_0(self.freq/1000000)
        self.set_variable_static_text_0_0_0((self.freq+self.doppler_shift)/1000000)
        self.satisfi_predict_query_0.set_freq(self.freq)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.freq)

    def get_sat(self):
        return self.sat

    def set_sat(self, sat):
        self.sat = sat
        self.set_audio_filename(('/home/jspark/data/audio/' + self.timestamp + '_' + self.sat + '.wav').replace(" ","_"))
        self.set_variable_static_text_0_0(self.sat)
        self.satisfi_predict_query_0.set_name(self.sat)

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        self.set_audio_filename(('/home/jspark/data/audio/' + self.timestamp + '_' + self.sat + '.wav').replace(" ","_"))

    def get_doppler_shift(self):
        return self.doppler_shift

    def set_doppler_shift(self, doppler_shift):
        self.doppler_shift = doppler_shift
        self.set_variable_static_text_0_0_0((self.freq+self.doppler_shift)/1000000)
        self.set_variable_static_text_0(self.doppler_shift)
        self.analog_sig_source_x_0.set_frequency(-self.doppler_shift)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_variable_static_text_0_0_0_0(self):
        return self.variable_static_text_0_0_0_0

    def set_variable_static_text_0_0_0_0(self, variable_static_text_0_0_0_0):
        self.variable_static_text_0_0_0_0 = variable_static_text_0_0_0_0
        self._variable_static_text_0_0_0_0_static_text.set_value(self.variable_static_text_0_0_0_0)

    def get_variable_static_text_0_0_0(self):
        return self.variable_static_text_0_0_0

    def set_variable_static_text_0_0_0(self, variable_static_text_0_0_0):
        self.variable_static_text_0_0_0 = variable_static_text_0_0_0
        self._variable_static_text_0_0_0_static_text.set_value(self.variable_static_text_0_0_0)

    def get_variable_static_text_0_0(self):
        return self.variable_static_text_0_0

    def set_variable_static_text_0_0(self, variable_static_text_0_0):
        self.variable_static_text_0_0 = variable_static_text_0_0
        self._variable_static_text_0_0_static_text.set_value(self.variable_static_text_0_0)

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

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
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)

    def get_notch_width(self):
        return self.notch_width

    def set_notch_width(self, notch_width):
        self.notch_width = notch_width
        self._notch_width_slider.set_value(self.notch_width)
        self._notch_width_text_box.set_value(self.notch_width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.notch_width / 2, 500, firdes.WIN_HAMMING, 6.76))

    def get_notch_freq(self):
        return self.notch_freq

    def set_notch_freq(self, notch_freq):
        self.notch_freq = notch_freq
        self._notch_freq_slider.set_value(self.notch_freq)
        self._notch_freq_text_box.set_value(self.notch_freq)
        self.analog_sig_source_x_0_1.set_frequency(-self.notch_freq)

    def get_audio_filename(self):
        return self.audio_filename

    def set_audio_filename(self, audio_filename):
        self.audio_filename = audio_filename

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(437365000),
        help="Set freq [default=%default]")
    parser.add_option("", "--sat", dest="sat", type="string", default="24278",
        help="Set sat [default=%default]")
    (options, args) = parser.parse_args()
    tb = auto_gs_cw(freq=options.freq, sat=options.sat)
    tb.Start(True)
    tb.Wait()

