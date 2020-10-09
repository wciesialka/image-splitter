import argparse
import src.ImageSplitter as ImageSplitter

def main(args):
    data = args['f'].read()
    args['f'].close()
    splitter = ImageSplitter.ImageSplitter(data,dpi=args['dpi'],paper_w=args['paperwidth'],paper_h=args['paperheight'])
    splitter.split(cols=args['columns'],rows=args['rows'],scale=(not args['noscale']))
    out = splitter.export()
    with args['output'] as f:
        f.write(out)
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Split image into n*k images and serve as a printable PDF.")
    parser.add_argument('f',metavar='Image', type=argparse.FileType('rb'), help="Path to image to process.")
    parser.add_argument('-n', '--columns', type=int, help="Number of columns.",default=3)
    parser.add_argument('-k', '--rows', type=int, help="Number of rows.", default=3)
    parser.add_argument('-s','--noscale',action='store_true',default=False,help="Disable automatic scaling.")
    parser.add_argument('-d','--dpi',type=float,help="DPI.",default=300)
    parser.add_argument('-w','--paperwidth',type=float,help="Specify Paper Width in inches.",default=8.5)
    parser.add_argument('-y','--paperheight',type=float,help="Specify Paper Height in inches.",default=11)
    parser.add_argument('-o','--output',type=argparse.FileType('wb'), help="Output file",default=open("out.pdf","wb"))
    args = parser.parse_args()
    main(vars(args))