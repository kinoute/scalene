import signal


class ScaleneSignals:

    start_profiling_signal = signal.SIGILL
    stop_profiling_signal = signal.SIGWINCH
    cpu_signal = signal.SIGVTALRM
    cpu_timer_signal = signal.ITIMER_REAL
    memcpy_signal = signal.SIGPROF
    # Malloc and free signals are generated by include/sampleheap.hpp.
    malloc_signal = signal.SIGXCPU
    free_signal = signal.SIGXFSZ
