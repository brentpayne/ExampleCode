'''
This main takes the sample means and variances for two populations 
and calculates the t-test that the first population's mean is 
greater than the second population 

@author: brent payne
'''
import os, sys
from pprint import pprint
from optparse import *
from bp_file import open_file_proper
from random import *
from math import *
         
def ttest_two_means_onetail(mu1, s1, n1, mu2, s2, n2):
    '''
    given: the means (mu), sample standard deviation (s), and sample sizes (n) for two populations
    return: the significance value of the first mean being greater than the second
    '''
    df = (((s1**2)/n1+(s2**2)/n2)**2)/(((s1**2)/n1)**2/(n1-1)+((s2**2)/n2)**2/(n2-1))
    t_numerator = mu1-mu2
    standard_error = sqrt(s1**2/n1+s2**2/n2)
    tscore = t_numerator/standard_error #<-- guess, need to lookup 
    return (df,tscore)

def main(argv=sys.argv):
    parser = OptionParser()
    parser.add_option("-m", "--mean1", dest="mean1", help="sample mean for 1st population", type="float")
    parser.add_option("-n", "--mean2", dest="mean2", help="sample mean for 2nd population", type="float")
    parser.add_option("-a", "--samplesize1", dest="samplesize1", help="sample size for 1st population", type="int")
    parser.add_option("-b", "--samplesize2", dest="samplesize2", help="sample size for 2nd population", type="int")
    #parser.add_option("-v", "--var1", dest="variance1", help="sample variance for 1st population", type="float")
    #parser.add_option("-w", "--var2", dest="variance2", help="sample variance for 2nd population", type="float")
    parser.add_option("-s", "--std1", dest="std1", help="sample standard deviation for 1st population", type="float")
    parser.add_option("-t", "--std2", dest="std2", help="sample standard deviation for 2nd population", type="float")
    
    (options, args) = parser.parse_args()
    print ttest_two_means_onetail(options.mean1, options.std1, options.samplesize1, options.mean2, options.std2, options.samplesize2)

if __name__ == '__main__':
    main(sys.argv)
