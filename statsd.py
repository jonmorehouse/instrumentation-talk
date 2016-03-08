import tornado.web

from statsd import StatsClient


class TranscoderJob(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def post(self):
        ###
        # create a new job
        ###
        statsd.incr('transcoder_job_created')
        self.finish('ok')
