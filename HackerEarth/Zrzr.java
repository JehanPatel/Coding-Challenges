import java.util.*;
public class ZrZr {
	public static void main(String[] arg){
		Scanner sc=new Scanner(System.in);
		StringBuffer sb=new StringBuffer();
		int t=sc.nextInt();
		while (t-->0){
			long n=sc.nextLong();
			sb.append(((n/5)+(n/25))+"\n");
		}
		System.out.println(sb);
		
	}
}