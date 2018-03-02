#ifdef __i386__
#include "i386/glibconfig.h"
#elif defined(__ppc__)
#include "ppc/glibconfig.h"
#elif defined(__x86_64__)
#include "x86_64/glibconfig.h"
#elif defined(__arm__)
#include "arm/glibconfig.h"
#else
#error "Unsupported Architecture"
#endif
