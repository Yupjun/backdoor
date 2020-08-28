import tensorflow as tf
#tf.compat.v1.disable_v2_behavior()

class Logger(object):
    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""
        #tf.summary.FileWriter(log_dir)
        self.writer = tf.summary.create_file_writer('log_dir') 

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""
        with self.writer.as_default():
            self.writer.add_summary(summary, step)
            self.writer.flush()

    def list_of_scalars_summary(self, tag_value_pairs, step):
        """Log scalar variables."""
        with self.writer.as_default():
            for tag, value in tag_value_pairs:
                tf.summary.scalar(tag,value,step=step)
            self.writer.flush()